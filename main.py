#!/bin/python
# -*- coding: utf8 -*-
print("\thi! receiver started!")

import socket, json
sock = socket.socket()
sock.bind(('', 8081))
sock.listen(5)
conn, addr = sock.accept()

try:
    with open("stored_values.json", "r") as read_file:
        values = json.load(read_file)
except BaseException:
    print("\tempty or no file!")
    values = []

print("new client:", addr)
while True:
    data = conn.recv(1024)
    if not data:
        break
    print("RECEIVED: ",data, "FORMATTED:", float(data.decode()))
    values.append(float(data.decode()))

conn.close()
print("writing...")
with open("stored_values.json", "w") as read_file:
    json.dump(values, read_file)
print("written successfully!\n\tbye")
