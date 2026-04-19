from socket  import *
from constCS import * #-
import math
import json
import threading

s = socket(AF_INET, SOCK_STREAM) 
s.bind(('0.0.0.0', PORT))  #-
s.listen(50)           #-

def handle_req(conn):
    data = conn.recv(1024)   # receive data from client
    if not data:
        conn.close()	
        return 
    dados = bytes.decode(data)
    array = json.loads(data)
    operation = array[0]
    op1 = array[1]
    op2 = array[2]
    res = None

    if(operation == 0): res = op1 + op2
    elif(operation == 1): res = op1 - op2
    elif(operation == 2): res = op1 * op2
    print("Data recieved from client: " + dados)
    conn.send(str.encode(str(res)))
    conn.close()
	
threads = []

while True:                # forever
    (conn, addr) = s.accept()  # returns new socket and addr. client 
    t = threading.Thread(target=handle_req, args=(conn,))
    t.start()
    threads.append(t)
