# Attack Collection


## Attacks

### Attack 1

**Description**

The attack assumes that both PLCs and HMIs are accessible on the Internet.
This attack is a DoS on pump P-101 governed by PLC-1 to achieve a overflow of tank T-201.

-   When the level of tank T-201 reaches the high setpoint of 80 gallons, the attacker forces the pump to remain on.
-   To accomplish this, the attacker uses a script that performs the following actions:
    -   Transmits a Modbus packet to read the analog input register associated with the level of tank T-101.
    -   When the level of tank T-101 reaches 80 gallons, the script continuously sends a different Modbus packet with the function code "write single discrete output coil" 0x05 to set the PLC register associated with pump P-101 to True.
-   As a result, the attacker can achieve an overflow of tank T-201 regardless of the state of valve MV-301.

**How to perform the attack**

To perform the attack described above on your attacker machine:

1.  Navigate to the `attacks/attack1` folder.

>**Note: If you wish to continue please keep in mind that the authors of this project do not condone any malicious use of the information provided and will not be held responsible for any damages resulting from such actions.**

2.  Modify the IP address of PLC1 with the public IP address of your own PLC1.
3.  Launch the attack by running the `python attack1.py` command.

### Attack 2

**Description**

In this attack, we assume that the HMI is exposed on the Internet. (Note that the HMI container hosts ScadaBR, version 1.0CE.)
The attacker exploits the authenticated arbitrary file upload vulnerability CVE-2021-26828 of ScadaBR to gain complete control of the HMI and carry out a MITM attack to cause the physical system to deadlock.
By exploiting CVE-2021-26828 combined with the use of default credential vulnerability, the attacker gains a web shell on the container. This, in turn, grants remote command execution, which is exploited to upload a statically linked Golang binary that does the following:
1.  It keeps transmitting a Modbus packet, with function code read discrete output coil 0x01, to read the PLC register associated with valve MV-301.
2.  It sends a second Modbus packet, with function code read analog input register 0x04, to read the PLC register associated with the level of tank T-101.
3.  Finally, when the level of the tank approaches the value 80 Gallons and the valve is still closed, the attacker drops all Modbus packets transmitted from PLC-2 to PLC-1 to intercept all requests to open valve MV-301.
4.  As a consequence, the valve remains closed and, in the long run, the system reaches the following deadlock state: tank T-201 is full (without overflow), and tanks T-202 and T-203 both face underflow.

**How to perform the attack**

To perform the attack described above on your attacker machine:

1.  Make sure Go is installed on your system. You can check if it's installed by running the command `go version` in a terminal window. If Go is not installed, you can download it from the official website: [https://golang.org/dl/](https://golang.org/dl/)
    
2.  Clone the `arpfox` repository from Github by running the following command in your terminal window:
    
    bashCopy code
    
    `git clone https://github.com/malfunkt/arpfox.git` 
    
3.  Navigate to the `arpfox` directory by running the following command:
    
    bashCopy code
    
    `cd arpfox` 
    
4.  Build the executable by running the following command:
    
    goCopy code
    
    `go build .` 
    
    This command will build the executable in the current directory.
    
5.  To extract the executable, navigate to the directory where the executable is located (`arpfox` directory in this case). You can copy or move the executable to another directory if you want.

>**Note: If you wish to continue please keep in mind that the authors of this project do not condone any malicious use of the information provided and will not be held responsible for any damages resulting from such actions.**

6.  Download the exploit from [https://www.exploit-db.com/exploits/49735](https://www.exploit-db.com/exploits/49735)
2.  Open a listener on the attacker machine to receive the reverse shell connection from the target machine
3.  Launch the exploit, providing the public IP of the HMI as input
4.  Upload the `arpfox` executable and the Python script, along with the necessary libraries, through the reverse shell
5.  Launch the Python script
6.  Once the Python script outputs "Begin the attack", execute the `arpfox` binary to divert the communication between PLC1 and PLC2.

### Attack 3

**Description**

In this attack, we assume that our honeynet is under a compromised VPN, and the attacker aims to perform a stealthy DoS attack on pump P-102 that is controlled by PLC3. The attack involves forcing the pump to continue working even when the tank T-203 reaches the low setpoint 0 Gallons, leading to the eventual breakdown of the pump.

The attacker accomplishes this by utilizing a script that continuously transmits Modbus packets with the function code "read analog input register 0x04" to read the PLC register linked to the tank T-203's level. Once the tank level reaches the low3 setpoint, the script sends a different Modbus packet with the function code "write single discrete output coil 0x05" to manipulate the PLC register associated with pump P-102, forcing it to remain on even in the absence of water.

To remain undetected, the attacker sets up a Man-in-the-Middle (MITM) attack and sends Modbus packets to the HMI interface indicating that the pump is off (function code "write single discrete output coil 0x05"), while it is actually still running. This attack aims to deceive operators into thinking that everything is working normally while the pump continues to work, leading to its eventual breakdown.

**How to perform the attack**

1. Connect to the compromised VPN.

>**Note: If you wish to continue please keep in mind that the authors of this project do not condone any malicious use of the information provided and will not be held responsible for any damages resulting from such actions.**


1.  Use the script attacks/attack3/attack3-capture.py to keep transmitting a Modbus packet, with function code read analog input register 0x04, to read the PLC registers and coils and saves the values in JSON format.
    
2.  Once the level reaches the value 0 Gallons, keep transmitting a different Modbus packet, with function code write single discrete output coil 0x05, to manipulate the PLC register associated with pump P-102. This will force the pump to remain on, even in the absence of water, and eventually break.
    
3.  To remain stealthy, set up a MITM attack using the binary previously built and starts the python script attacks/attack3/attack3-server.py that serves the values previously recorded.
    

## Disclaimer

The attack files presented in this paper are intended for demonstration purposes only. They should not be used to harm real Industrial Control Systems (ICS). The authors of this paper do not condone any malicious use of the information provided and will not be held responsible for any damages resulting from such actions.

## License

This repository is licensed under the MIT License. See the LICENSE file for more information.
