import socket
import threading
import os
import time
from queue import Queue

HOST = '192.168.1.211'
PORT = 9705

NUMBEROFTHREADS = 2
JOBNUMBER = [1,2]

queue = Queue()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
NAMEOFPC = socket.gethostname()
CLIENTADDRESS = str(socket.gethostbyname(NAMEOFPC))
print(CLIENTADDRESS, type(CLIENTADDRESS))


def socket_connect(username):
    """ Connect to a remote socket """
    try:
        s.connect((HOST, PORT))
        s.send(str.encode(username))
    except socket.error as e:
        print("Socket connection error: " + str(e))
        time.sleep(5)
        raise

def sendMessage(clientto, message):
    
    #sends the name of the client they want to send it to
    s.send(str.encode(CLIENTADDRESS + '\t'+ clientto + '\t' + message))#Sends the message to the server in 'tab' format

def socket_close():
    s.close()


def receiveMessages():
    try:
        message1 = s.recv(4096)
        message1 = message1.decode('utf-8')
        print('\n'+message1+'\n')
    except BlockingIOError:
        pass
    if len(message1) > 0:
        return message1
    else:
        return None
'''
def createworkers():
    for _ in range(NUMBEROFTHREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

def work():

    x = queue.get()
    if x == 1:
        sendMessage()
    if x == 2:
        receiveMessages()

    queue.task_done()

def createJobs():
    for x in JOBNUMBER:
        queue.put(x)
    queue.join()




def sign_up():
    username = input('Enter your username')
    password = input('Enter your password')
    if username:
        socket_connect(username)
    else:
        print('Error')
    while True:
        createworkers()
        createJobs()

    s.close()
def log_in():
    pass

def main():
    choice = input('Do you want to sign up or log in: ')
    if choice == '1':
        sign_up()
    elif choice == '2':
        log_in()
    else:
        main()

main()
'''