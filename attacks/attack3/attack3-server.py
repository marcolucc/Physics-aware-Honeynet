from pymodbus.server.sync import StartTcpServer
from pymodbus.datastore import ModbusSlaveContext, ModbusSequentialDataBlock, ModbusServerContext
import json

# Define the filename containing the data
JSON_FILENAME = 'data.json'

# Define the Modbus server address and port number
SERVER_ADDRESS = 'localhost'
SERVER_PORT = 502

# Load the initial data from the JSON file
with open(JSON_FILENAME, 'r') as f:
    data = json.load(f)

# Define the Modbus data blocks
coil_block = ModbusSequentialDataBlock(data['coil_value'], [0])
register_block = ModbusSequentialDataBlock(data['register_value'], [0])

# Define the Modbus slave context
slave_context = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(data['coil_value'], [0]),
    ir=ModbusSequentialDataBlock(data['register_value'], [0]),
)

# Define the Modbus server context
server_context = ModbusServerContext(slaves=[slave_context], single=True)

# Define the Modbus server
server = StartTcpServer(server_context, address=(SERVER_ADDRESS, SERVER_PORT))

# Load the new data from the JSON file and update the Modbus data blocks
def update_data():
    with open(JSON_FILENAME, 'r') as f:
        data = json.load(f)
    coil_block.setValues(0, [data['coil_value']])
    register_block.setValues(0, [data['register_value']])

# Continuously update the Modbus data blocks with new data from the JSON file
while True:
    update_data()
    server_context[0].setValues('di', 0, coil_block)
    server_context[0].setValues('ir', 0, register_block)
