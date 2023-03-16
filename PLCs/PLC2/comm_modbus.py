import easymodbus.modbusClient
import time

#wait for plc to be ready
time.sleep(5)
stop_flag1 = False
stop_flag2 = False

while (not stop_flag1):
    #print("connessione plc1")
    try:
        plc1 = easymodbus.modbusClient.ModbusClient('plc1.rete', 502)
        plc1.connect()
        stop_flag1 = True
    except:
        print("errore connessione plc1")
        time.sleep(1)

while (not stop_flag2):
    #print("connessione plc2")
    try:
        plc2 = easymodbus.modbusClient.ModbusClient('localhost', 502)
        plc2.connect()
        stop_flag2 = True
    except:
        print("errore connessione plc2")
        time.sleep(1)


while (True):
    #print("leggo")
    #leggo i registri di input (level e request)
    
    try:
        #print("leggo da plc2")
        inputRegisters = plc2.read_coils(0, 1)
        #print(inputRegisters)
    except:
        print("Errore in lettura coil")

    try:
        #print("\n Richiesta: ")
        richiesta = inputRegisters[0]
    
        print(richiesta)
    except:
        print("errore lettura buffer registro")
    

    #scrivo i coil di richiesta
    #print("Scrivo su plc1")
    try:
        plc1.write_single_coil(2, richiesta)

        plc1.read_coils(2, 1)
    except:
        print("errore scrittura")
    #print("close connection")
    time.sleep(1)
    
