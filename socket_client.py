import socket
import os
def client():
    host=socket.gethostbyname('localhost')
    port =5000
    f=open("filename","r")
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print(f"[+] connecting to {host}:{port}")
    s.connect((host,port))
    print("Connected......")
    while True:
        data=f.read()
        if not data:
            break
        while data:
            s.send(str(data).encode())
            data=f.read()
    s.close()
if __name__=='__main__':
    client()