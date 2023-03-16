//apt-get install libmodbus
#include <iostream>
#include <modbus/modbus.h>
#include <unistd.h>

int main()
{
    // Wait for PLC to be ready
    sleep(5);

    bool stop_flag1 = false;
    bool stop_flag2 = false;

    modbus_t* plc1;
    modbus_t* plc2;

    while (!stop_flag1)
    {
        // Connect to plc1
        plc1 = modbus_new_tcp("plc1.rete", 502);
        if (modbus_connect(plc1) == -1)
        {
            std::cout << "Errore connessione plc1" << std::endl;
            modbus_free(plc1);
            sleep(1);
        }
        else
        {
            stop_flag1 = true;
        }
    }

    while (!stop_flag2)
    {
        // Connect to plc2
        plc2 = modbus_new_tcp("localhost", 502);
        if (modbus_connect(plc2) == -1)
        {
            std::cout << "Errore connessione plc2" << std::endl;
            modbus_free(plc2);
            sleep(1);
        }
        else
        {
            stop_flag2 = true;
        }
    }

    uint8_t inputRegisters[1];

    while (true)
    {
        try
        {
            // Read input registers from plc2
            modbus_read_bits(plc2, 0, 1, inputRegisters);

            bool richiesta = inputRegisters[0];
            std::cout << richiesta << std::endl;
        }
        catch (...)
        {
            std::cout << "Errore in lettura coil" << std::endl;
        }

        try
        {
            // Write request to plc1
            modbus_write_bit(plc1, 2, richiesta);
            modbus_read_bits(plc1, 2, 1, inputRegisters);
        }
        catch (...)
        {
            std::cout << "Errore scrittura" << std::endl;
        }

        sleep(1);
    }

    modbus_close(plc1);
    modbus_free(plc1);

    modbus_close(plc2);
    modbus_free(plc2);

    return 0;
}
