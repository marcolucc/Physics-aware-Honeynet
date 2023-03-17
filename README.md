
# HoneyICS: A High-interaction Physics-aware Honeynet for Industrial Control Systems

This repository contains the source code and necessary files for the paper "HoneyICS: A High-interaction Physics-aware Honeynet for Industrial Control Systems".

## Abstract

Industrial control systems (ICSs) are vulnerable to cyber-physical attacks, i.e., security breaches in cyberspace that adversely affect the underline physical processes. In this context, honeypots are ideal countermeasures both to defend against such attacks and discover new attack strategies. In recent years, Honeypots for ICSs have made several progresses in trying to faithfully reproduce the behavior of OT networks, including physical process interactions. We propose a high-interaction, physics-aware, scalable, and extensible honeynet for ICSs, equipped with an advanced monitoring system. We deployed our honeynet on the Internet and conducted experiments to compare it with existing ICS honeypots.


## Contents

This repository contains the following directories:

### PLCs

This directory contains the source code to build the software PLC that can be used in the honeynet. The PLCs' codes are implemented in ladder logic and are designed to simulate the behavior of real-world ICSs.

### Proxy

This directory contains the source code for the proxy servers used in the honeynet. The proxies are responsible for forwarding traffic between the PLCs.

### Matlab Simulink

This directory contains the source code for the Matlab Simulink models used in the honeynet. The models are used to simulate the physical processes controlled by the PLCs.

### Attacks

This directory contains the attack files used in the experiments conducted in the paper. The directory is further divided into subdirectories for each attack. Each subdirectory contains the necessary files to execute the attack, including scripts, payloads, and configuration files.

## Setup

![Alt text](image_url)
### Prerequisites for the honeynet
1. Make sure your system meets the requirements for installing Docker.
2. Install Docker:
    1. Update your package manager’s index:
        - On Ubuntu: `sudo apt-get update`
        - On Fedora: `sudo dnf check-update`
    2. Install Docker Engine:
        - On Ubuntu: `sudo apt-get install docker-ce docker-ce-cli containerd.io`
        - On Fedora: `sudo dnf install docker-ce docker-ce-cli containerd.io`

3. Verify installation: Open a terminal or command prompt and run the command `docker --version` to verify that Docker has been installed successfully.

4. Install Kibana and Elastic:
    1. Pull Elasticsearch image: In a terminal session, pull the Elasticsearch image from Docker Hub by running the command: `docker pull docker.elastic.co/elasticsearch/elasticsearch:8.6.2`
    
    2. Start Elasticsearch container: Start an Elasticsearch container by running the command: `docker run --name es-01 -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:8.6.2`
    
    3. Pull Kibana image: In a new terminal session, pull the Kibana image from Docker Hub by running the command: `docker pull docker.elastic.co/kibana/kibana:8.6.2`

    4. Start Kibana container: Start a Kibana container and connect it to your Elasticsearch container by running the command: `docker run --name kib-01 --net elastic -p 5601:5601 docker.elastic.co/kibana/kibana:8.6.2`

5. Install IPtables:

    1.  **Update package manager:**  Update your package manager by running the command: ` sudo apt update`
        
    2.  **Install iptables:**  Install iptables by running the command: `sudo apt install iptables`
        
    3.  **Check iptables status:**  Check the status of your current iptables configuration by running the command: `sudo iptables`

### Prerequisites for the attacker
In order to properly configure the attacker machine for the purposes of this experiment, it is necessary to install and set up several specific tools and libraries. These include:
- Python
- Pymodbus
- Easymodbus
- Dsniff
- IPtables
- OpenVPN client


#### Python
1.  **Update package manager:**  Update your package manager by running the command: ` sudo apt update `
    
2.  **Install Python versions:**  Install both versions of Python by running their respective commands:
    
    -   For Python 3.7:  `sudo apt install python3.7`
    -   For Python 2.7:  `sudo apt install python2.7`
3.  **Install pip:**  Install pip for both versions of Python by running their respective commands:
    
    -   For Python 3.7:  `sudo apt install python3-pip`
    -   For Python 2.7:  `sudo apt install python-pip`

4. **Check if everything is installed correctly** by running the following commands:

    1.  **Check Python versions:**  Check the installed versions of Python by running their respective commands:
        
        -   For Python 3.7:  `python3.7 --version`
        -   For Python 2.7:  `python2.7 --version`
    2.  **Check pip versions:**  Check the installed versions of pip by running their respective commands:
        
        -   For pip3:  `pip3 --version`
        -   For pip2:  `pip2 --version`
## Usage

To use the source code and attack files in this repository, follow these steps:

1.  Clone the repository to your local machine.
2.  Install the necessary dependencies for the PLCs, proxy servers, and Matlab Simulink models.
3.  Configure the honeynet according to your needs.
4.  Run the honeynet.
5.  Execute the attack files to test the honeynet's effectiveness.

## Disclaimer

The attack files presented in this paper are intended for demonstration purposes only. They should not be used to harm real Industrial Control Systems (ICS). The authors of this paper do not condone any malicious use of the information provided and will not be held responsible for any damages resulting from such actions.

## License

This repository is licensed under the MIT License. See the LICENSE file for more information.
