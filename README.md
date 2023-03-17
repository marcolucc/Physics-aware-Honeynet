
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

## Usage

To use the source code and attack files in this repository, follow these steps:

1.  Clone the repository to your local machine.
2.  Install the necessary dependencies for the PLCs, proxy servers, and Matlab Simulink models.
3.  Configure the honeynet according to your needs.
4.  Run the honeynet.
5.  Execute the attack files to test the honeynet's effectiveness.

## License

This repository is licensed under the MIT License. See the LICENSE file for more information.
