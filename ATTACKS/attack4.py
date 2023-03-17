from easymodbus.modbusClient import ModbusClient
import time

# Set up Modbus client
client = ModbusClient("plc1.rete", 502) # IP address and port of Modbus server
client.connect()

# Loop to rapidly open and close coil
while True:
    client.write_single_coil(0, True)
    time.sleep(0.1) # Wait for 0.1 seconds
    client.write_single_coil(0, False)
    time.sleep(0.1) # Wait for 0.1 seconds

# Disconnect from Modbus server (this will never happen since the loop is infinite)
client.close()
