import  subprocess

o = subprocess.check_output("pkill -f shadowsocks-server", shell=True)
print o


o = subprocess.check_output("nohup /home/ubuntu/shadowsocks-server -p 443 -k applemac -m aes-128-cfb &", shell=True)
print o

