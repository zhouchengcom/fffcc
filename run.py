import  subprocess


try:
    o = subprocess.check_output("pkill -f shadowsocks-server", shell=True)
    print o
except Exception as e:
    print e
    

try:
    o = subprocess.check_output("nohup /home/ubuntu/shadowsocks-server -p 443 -k applemac -m aes-128-cfb &", shell=True)
    print o
except Exception as e:
    print e

