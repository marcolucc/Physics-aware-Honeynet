from pymodbus.client.sync import ModbusTcpClient

# Set up the Modbus client
client = ModbusTcpClient('192.168.10.116', port=502)

# Connect to the Modbus server
client.connect()

while True:
    # Read an input register (address 100) from the Modbus server
    result = client.read_input_registers(address=0, count=1, unit=1)

    if result.isError():
        # Handle any errors that occurred
        print(f"Error reading input register: {result}")
    else:
        # Print the value of the input register
        value = result.registers[0]
        print(f"Input register value: {value}")

        # Check if the input register value is 80
        if value == 80:
            while True:
                # Set a coil to true (address 200) on the Modbus server
                result = client.write_coil(address=0, value=True, unit=1)

                if result.isError():
                    # Handle any errors that occurred
                    print(f"Error setting coil: {result}")
                else:
                    # Print a message to confirm that the coil was set
                    print("Coil set successfully")
        else:
            # Print a message to indicate that the input register value was not 80
            print("Input register value is not 80")

# Disconnect from the Modbus server
client.close()