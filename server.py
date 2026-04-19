from socket  import *
from constCS import * #-
import math
import json
import threading

s = socket(AF_INET, SOCK_STREAM) 
s.bind(('0.0.0.0', PORT))  #-
s.listen(1)           #-

def handle_req(data, conn):
    dados = bytes.decode(data)
    array = json.loads(data)
    operation = array[0]
    op1 = array[1]
    op2 = array[2]
    res = None

    if(operation == 0): res = op1 + op2
    elif(operation == 1): res = op1 - op2
    elif(operation == 2): res = op1 * op2
    print("Data recieved from client: " + bytes.decode(data))
    conn.send(str.encode(str(res)))

threads = []

(conn, addr) = s.accept()  # returns new socket and addr. client 
while True:                # forever
    data = conn.recv(1024)   # receive data from client
    if data:
      t = threading.Thread(target=handle_req, args=(data, conn))
      threads.append(t)
      t.start()
    else: 
      conn.close()
      break

for thr in threads:
    thr.join()
