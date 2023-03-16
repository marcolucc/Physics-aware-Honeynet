#!/bin/bash

# Run the first script in the background
/bin/bash /home/ScadaBR_Installer/run.sh &

# Run the second script in the background
/bin/bash /home/selenium/host.sh &

# Wait for both scripts to finish
wait

echo "Both scripts have finished executing."
