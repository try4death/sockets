import socket

def server():
    host=socket.gethostbyname('localhost')
    port = 5000
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind((host,port))
    except Excpetion as e:
        print(e)
    while True:
        s.listen()
        conn,addr=s.accept()
        f=open('filename',"w+")
        print(addr)
        while True:
            data=conn.recv(1024).decode()
            if not data:
                break
            else:
                f.write(data)
                f.close()
if __name__=='__main__':
    server()
