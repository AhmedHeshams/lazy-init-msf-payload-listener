import re
import socket 
import subprocess
import os
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
    try:
        #ceck if there's someone work in 8080 port , if we find it we kill it 
        output= subprocess.check_output(["lsof","-i",":8080"],stderr=subprocess.STDOUT,shell=False)
        output = output.split(" ")[21]
        subprocess.check_output(["kill",output],stderr=subprocess.STDOUT,shell=False)
    except:
        pass
    os.system("gnome-terminal -x msfconsole -r andpay.rc")

