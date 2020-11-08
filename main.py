#!/bin/python
# -*- coding: utf8 -*-
import socket, json, time
print("\thi! receiver started!")

values = dict()
#open
try:
    with open("stored_values.json", "r") as read_file:
        values.update(json.load(read_file))
except BaseException:
    print("\tempty or no file!")

sock = socket.socket()
sock.bind(('', 8082))
sock.listen(5)

while True:
    conn, addr = sock.accept()
    print("\nnew client:", addr)
    #read socket
    while True:
        data = conn.recv(1024)
        if not data:
            break
        # print("RECEIVED: ",data, "FORMATTED:", float(data.decode()))
        #push vars to storage
        payload = json.loads(data.decode())
        values[time.ctime()] = {
            "temp": float(payload[0]),
            "humid": float(payload[1]),
            "flower": float(payload[2])
            }

    #close and save
    conn.close()
    print("writing...", payload)
    with open("stored_values.json", "w") as read_file:
        json.dump(values, read_file)
    print("written successfully!\n")
