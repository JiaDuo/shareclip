#!/usr/bin/env python
import socket
import threading
import time
import pyperclip
import traceback

perip=open('config.ini').readline().strip()
print perip
port=9999
clipdata=pyperclip.paste()


def tcplink(sock,addr):
    global clipdata
    print 'Accept new connection from %s:%s...' % addr
    while True:
        data=sock.recv(1024*10)
        time.sleep(1)
        if data=='exit' or not data:
            break
        #sock.send('Hello,%s!'%data)
        print "%s - %s"%("recv",data)
        try:
            pyperclip.copy(data)
            clipdata = data
        except Exception as e:
            traceback.print_exc()
    sock.close()
    print 'Connection from %s:%s closed.'%addr

def clipbord_recv_server():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(('0.0.0.0',port))
    s.listen(5)
    while True:
        sock,addr = s.accept()
        t=threading.Thread(target=tcplink,args=(sock,addr))
        #t.setDaemon(True)
        t.start()

def clipbord_send():
    global clipdata
    while True:
        data = pyperclip.paste()
        if data != clipdata:
            try:
                s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((perip,port))
                s_data = data
                s.send(s_data)
                clipdata = data
                print "%s - %s"%("send",s_data)
            except Exception :
                traceback.print_exc()
            finally:
                s.close()
        time.sleep(1)

def test():
    while True:
        print "running"
        time.sleep(10)

if __name__ == "__main__":
    threads = []
    t1 = threading.Thread(target=clipbord_send)
    t2 = threading.Thread(target=clipbord_recv_server)
    t3 = threading.Thread(target=test)
    threads = [t1,t2,t3]
    for t in threads:
        t.setDaemon(True)
        t.start()

    while True:
        time.sleep(1)
        pass
