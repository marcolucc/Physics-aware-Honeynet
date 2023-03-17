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
        plc1 = modbus_new_tcp("plc1.net", 502);
        if (modbus_connect(plc1) == -1)
        {
            std::cout << "Connection error PLC1" << std::endl;
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
            std::cout << "Connection error PLC2" << std::endl;
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

            bool req = inputRegisters[0];
            std::cout << req << std::endl;
        }
        catch (...)
        {
            std::cout << "coil reading error" << std::endl;
        }

        try
        {
            // Write request to plc1
            modbus_write_bit(plc1, 2, req);
            modbus_read_bits(plc1, 2, 1, inputRegisters);
        }
        catch (...)
        {
            std::cout << "Writing error" << std::endl;
        }

        sleep(1);
    }

    modbus_close(plc1);
    modbus_free(plc1);

    modbus_close(plc2);
    modbus_free(plc2);

    return 0;
}
