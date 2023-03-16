docker build -t simulink1 .
docker run -p 10001:10001/udp -p 10002:10002/udp -p 10003:10003/udp -p 10004:10004/udp 10005:10005/udp -p 10006:10006/udp --name simulink -td simulink 
docker exec -it simulink bash

