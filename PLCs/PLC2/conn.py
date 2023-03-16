from pyModbusTCP.client import ModbusClient

# create a Modbus TCP client instance
client = ModbusClient(host='localhost', port=502)

# connect to the Modbus TCP server
client.open()

# read the value of a single coil
result = client.read_coils(0, 1, unit=1)

# print the value of the coil
print(result[0])

# close the Modbus TCP connection
client.close()
