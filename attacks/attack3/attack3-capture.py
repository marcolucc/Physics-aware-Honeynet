from pymodbus.client.sync import ModbusTcpClient
import json
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

# Define the PLC address and port number
PLC_ADDRESS = 'plc3.net'
PLC_PORT = 502

# Define the register and coil addresses
REGISTER_ADDRESS = 100
COIL_ADDRESS = 200

# Define the filename to save the data to
JSON_FILENAME = 'data.json'

# Define the duration to capture data (in seconds)
CAPTURE_DURATION = 3600

# Define the class for the HTTP server
class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        with open(JSON_FILENAME, 'r') as f:
            data = json.load(f)
        self.wfile.write(json.dumps(data).encode())

# Define the function to capture the data and save it to a JSON file
def capture_data():
    client = ModbusTcpClient(PLC_ADDRESS, port=PLC_PORT)
    client.connect()

    # Read the values of the input register and coil
    register_value = client.read_input_registers(REGISTER_ADDRESS, count=1).registers[0]
    coil_value = client.read_coils(COIL_ADDRESS, count=1).bits[0]

    # Create a dictionary to store the data
    data = {
        'register_value': register_value,
        'coil_value': coil_value,
        'timestamp': int(time.time())
    }

    # Save the data to a JSON file
    with open(JSON_FILENAME, 'w') as f:
        json.dump(data, f)

    client.close()

# Start the data capture loop
start_time = time.time()
while (time.time() - start_time) < CAPTURE_DURATION:
    capture_data()
    time.sleep(1)

# Start the HTTP server to serve the captured data
server_address = ('', 502)
httpd = HTTPServer(server_address, HTTPRequestHandler)
httpd.serve_forever()
