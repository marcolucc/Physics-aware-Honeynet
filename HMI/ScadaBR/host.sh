#!/bin/bash

# Define the bindings
binding1="192.168.10.106  plc1.rete"
binding2="192.168.10.107  plc2.rete"
binding3="192.168.10.108  plc3.rete"

# Store the hosts file location
hosts_file="/etc/hosts"

# Check if the hosts file exists
if [ -f "$hosts_file" ]; then
  # Backup the original hosts file
  sudo cp "$hosts_file" "${hosts_file}.bak"

  # Add the bindings to the hosts file
  sudo echo "$binding1" >> "$hosts_file"
  sudo echo "$binding2" >> "$hosts_file"
  sudo echo "$binding3" >> "$hosts_file"

  echo "Hosts file updated successfully."
else
  echo "Error: Hosts file not found."
fi
