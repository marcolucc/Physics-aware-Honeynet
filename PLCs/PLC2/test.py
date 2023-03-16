import modbus_tk
import modbus_tk.defines as cst
import modbus_tk.modbus_tcp as modbus_tcp
import time

#wait for plc to be ready
time.sleep(5)

stop_flag1 = False
stop_flag2 = False

while not stop_flag1:
    try:
        #connect to plc1
        plc1 = modbus_tcp.TcpMaster('plc1.rete', 502)
        plc1.set_timeout(5.0)
        plc1.connect()
        stop_flag1 = True
    except:
        print("errore connessione plc1")
        time.sleep(1)

while not stop_flag2:
    try:
        #connect to plc2
        plc2 = modbus_tcp.TcpMaster('localhost', 502)
        plc2.set_timeout(5.0)
        plc2.connect()
        stop_flag2 = True
    except:
        print("errore connessione plc2")
        time.sleep(1)

while True:
    try:
        #read input registers from plc2
        inputRegisters = plc2.execute(1, cst.READ_COILS, 0, 1)
        richiesta = inputRegisters[0]
        print(richiesta)
    except:
        print("Errore in lettura coil")

    try:
        #write request to plc1
        plc1.execute(1, cst.WRITE_SINGLE_COIL, 2, output_value=richiesta)
        plc1.execute(1, cst.READ_COILS, 2, 1)
    except:
        print("errore scrittura")

    time.sleep(1)
