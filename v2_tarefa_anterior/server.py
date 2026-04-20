from socket import *
from constCS import *
import json

N_REQUESTS = 10000
processed = 0

s = socket(AF_INET, SOCK_STREAM)
s.bind(("0.0.0.0", PORT))
s.listen(50)

while processed < N_REQUESTS:
    conn, addr = s.accept()
    try:
        data = conn.recv(1024)
        if not data:
            continue

        operation, op1, op2 = json.loads(data)

        if operation == 0:
            res = op1 + op2
        elif operation == 1:
            res = op1 - op2
        elif operation == 2:
            res = op1 * op2
        else:
            res = "invalid operation"

        conn.send(str(res).encode())
        processed += 1
    finally:
        conn.close()

print(f"Processed {processed} requests")
s.close()
