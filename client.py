from socket  import *
from constCS import * #-
import random
import threading

NUM_REQUESTS = 10
threads = []

def send_req(operation, op1, op2):
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((HOST, PORT)) # connect to server (block until accepted)
    s.send(f"[{operation},{op1},{op2}]".encode()) 
    print("Sent operation 0, and operands 1,2 to server")
    data = s.recv(1024)     # receive the response
    print ("Resultado recebido do servidor: " + bytes.decode(data))            # print the result
    s.close()               # close the connection

for _ in range(0, NUM_REQUESTS):
    operation = random.randint(0, 2) 
    op1 = random.randint(1, 10) 
    op2 = random.randint(1, 10)
    t = threading.Thread(target=send_req, args=(operation, op1, op2))
    threads.append(t)
    t.start()

for thr in threads:
    thr.join()