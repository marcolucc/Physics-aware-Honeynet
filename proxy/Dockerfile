FROM nginx
RUN apt update && apt install procps net-tools iputils-ping vim iproute2 dnsutils tcpdump iptables -y
COPY nginx.conf /etc/nginx/nginx.conf