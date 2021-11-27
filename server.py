import socket
import time
import threading
from queue import Queue
import sys
import concurrent.futures

HOST = ''
PORT = 9705

NUMBEROFTHREADS = 2
JOB = [1,2]
queue = Queue()

allConnections = []
allAddress = []
clientAddresses = {}

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def socket_create():
    try:
        s.bind((HOST, PORT))
        s.listen(5)
    except socket.error as msg:
        print(f'Binding error {str(msg)}, retrying...')
        time.sleep(2)
        socket_create()

def socket_accept():
    
    while 1:
        conn, address = s.accept()
        conn.setblocking(0)#Asynchronous type
        allConnections.append(conn)
        allAddress.append(address)
        data = conn.recv(4096)
        userid = data.decode('utf-8')
        #When the database is created do select staffid/managerid from table where staffid/managerid = userid
        #then put that variable in clientAddresses[staffid/managerid] = conn
        clientAddresses[userid] = conn 
        print(clientAddresses)
        print(allAddress)


def receiveMessages():
    while True:
        for conn in allConnections:
            try:
                try:
                    data = conn.recv(4096)
                    if len(data) <= 0:
                            break
                    data = data.decode('utf-8')
                    clientsent = data.split('\t')#Splits the data to three parts
                    try:
                        clientsendfrom, clientsendto, message = clientsent[0], clientsent[1], clientsent[2]
                        #assigns the data to three variables
                        print(clientsendfrom, message, clientsendto)
                    except IndexError:
                        pass
                except ConnectionResetError:
                    continue
            except BlockingIOError:
                continue
            try:
                conn1 = clientAddresses[clientsendto]
                conn1.send(str.encode(message))
            except UnboundLocalError:
                continue
    s.close()


def createworkers():
    for _ in range(NUMBEROFTHREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

def work():

    x = queue.get()
    if x == 1:
        socket_create()
        socket_accept()
    if x == 2:
        receiveMessages()

    queue.task_done()


def createJobs():
    for x in JOB:
        queue.put(x)
    queue.join()


createworkers()
createJobs()


