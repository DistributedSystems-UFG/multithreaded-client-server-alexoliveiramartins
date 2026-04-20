from socket import *
from constCS import *
import random
import time

N_REQUESTS = 10000

start = time.time()

for _ in range(N_REQUESTS):
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((HOST, PORT))

    operation = random.randint(0, 2)
    op1 = random.randint(1, 10)
    op2 = random.randint(1, 10)

    s.send(f"[{operation},{op1},{op2}]".encode())
    s.recv(1024)
    s.close()

elapsed = time.time() - start
print(f"Sent {N_REQUESTS} requests in {elapsed:.4f}s")
