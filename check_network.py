import getpass
import sys
import telnetlib
import time
import re
import os

user = "muikaf"
password = "spoC3hiBa8"

def connect(host):
    global tn
    tn = telnetlib.Telnet(host,timeout=2)
    tn.read_until(b"Username:")
    tn.write(user.encode('ascii') + b"\n")
    if tn.read_until(b"Password:"):
        print ("YES")
    else:
        print ("NOT")
    tn.write(password.encode('ascii') +b"\n")
    #tn.read_until(b"#")


#a = input("Input rtr:")
#if a in routers:
a = {'10.126.0.36'}
#   HOST = routers[a] + ""
for i in a:
    response = os.system(f"ping -c 1 {i}")
    if (response == 0):
        connect(i)
    #tn.write("term wi 500 ".encode('ascii')+ b"\n")
    #tn.write("term length 0".encode('ascii')+ b"\n")
   #time.sleep(1)
        tn.write("show version".encode('ascii') + b"\n")
    #tn.write("exit".encode('ascii'))
        tn.write("term wi 500".encode('ascii') + b"\n")
        tn.write("term length 0".encode('ascii') + b"\n")
        tn.write("vi :ARPA-VPN".encode('ascii') + b"\n")
        tn.write("sh ip route".encode('ascii') + b"\n")
        time.sleep(15)
        tn.write("exit".encode('ascii') + b"\n")
    #tn.write("end".encode('ascii') + b"\n")
        print("Exit")
    #tn.read_until(b"Active after reboot")
        time.sleep(2)
    #print(tn.read_all())
        b = tn.read_all().decode('ascii')
        result = re.findall('8\d{1,2}.\d{2,3}.\d{2,3}.\d{1,3}\\/30',b)
        #result = re.findall('\d{2,3}.\d{2,3}.\d{2,3}.\d{1,3}\\/30\s{1,5}\w{3,7}',b)
        print(result[0])
        for t in len(result):
           a = t.split('.')
           a = a.split('/')
           
            
        #hostname = f'Host: {i} Name: '
        #find_hostname = re.search(r'\w*\d*-\w*\d*-swc\d{1,5}',b)
        #print(find_hostname[0])
        #f = open('result_check.txt','a')
        #b = b.split(' ')
        #f.write(f'Active{result[0]} Inactive{result[1]} {hostname}{find_hostname[0]}\n')
        #print(f'Active{result[0]} Inactive{result[1]} {hostname}{find_hostname[0]}')
        result.sort()
        #f.close()
        #print(f'{result}')
    else:
        print(f"Host {i} unavailable")