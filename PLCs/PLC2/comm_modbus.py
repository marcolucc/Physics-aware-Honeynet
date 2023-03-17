import easymodbus.modbusClient
import time

#wait for plc to be ready
time.sleep(5)
stop_flag1 = False
stop_flag2 = False

while (not stop_flag1):
    try:
        plc1 = easymodbus.modbusClient.ModbusClient('plc1.net', 502)
        plc1.connect()
        stop_flag1 = True
    except:
        print("error connection plc1")
        time.sleep(1)

while (not stop_flag2):
    try:
        plc2 = easymodbus.modbusClient.ModbusClient('localhost', 502)
        plc2.connect()
        stop_flag2 = True
    except:
        print("error connection plc2")
        time.sleep(1)


while (True):
    
    try:
        inputRegisters = plc2.read_coils(0, 1)
    except:
        print("coil reading error")

    try:
        req = inputRegisters[0]
    
        print(req)
    except:
        print("buffer reading error")
    
    try:
        plc1.write_single_coil(2, req)

        plc1.read_coils(2, 1)
    except:
        print("writing error")
    time.sleep(1)
    
