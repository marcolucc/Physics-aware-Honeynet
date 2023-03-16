#!bin/bash/

#cd /home/ScadaBR_Installer/
#sudo /opt/tomcat6/apache-tomcat-6.0.53/bin/startup.sh 
sudo /home/ScadaBR_Installer/update_scadabr.sh

FILE=/home/ScadaBR_Installer/started.txt
if ! [[ -f "$FILE" ]]; then
    echo "Don't remove this file" >> /home/ScadaBR_Installer/started.txt
    sudo python3 loaddata.py
fi 
    

while(true); do sleep 1000; done