import socket

# Define the Modbus function codes
READ_COILS = 0x01
READ_DISCRETE_INPUTS = 0x02
READ_HOLDING_REGISTERS = 0x03
READ_INPUT_REGISTERS = 0x04
WRITE_SINGLE_COIL = 0x05
WRITE_SINGLE_REGISTER = 0x06
WRITE_MULTIPLE_COILS = 0x0F
WRITE_MULTIPLE_REGISTERS = 0x10

# Define the Modbus address of the coil we want to serve
COIL_ADDRESS = 0x0000

# Define the value of the coil
COIL_VALUE = True

# Create a TCP socket to listen on port 502
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 502))
server_socket.listen(1)

# Loop forever and accept incoming connections
while True:
    conn, addr = server_socket.accept()
    print(f'Connection from {addr}')

    # Receive the Modbus request
    request = conn.recv(1024)
    if not request:
        continue

    # Extract the function code and address from the request
    function_code = request[7]
    address = int.from_bytes(request[8:10], byteorder='big')

    # If the function code is READ_COILS and the address matches our coil address,
    # return the value of the coil
    if function_code == READ_COILS and address == COIL_ADDRESS:
        response = bytearray([
            request[0], request[1], request[2], request[3], # Transaction ID
            request[4], request[5], request[6], request[7], # Protocol ID and function code
            0x01, # Byte count
            int(COIL_VALUE) # Coil value (True = 0xFF, False = 0x00)
        ])
        conn.send(response)

    # Close the connection
    conn.close()