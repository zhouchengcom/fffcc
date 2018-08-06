pkill -f shadowsocks-server
nohup /home/ubuntu/shadowsocks-server -p 443 -k applemac -m aes-128-cfb 1>/home/ubuntu/ss.log 2>/home/ubuntu/sse.log &
