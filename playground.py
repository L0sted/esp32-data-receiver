#!/bin/python

import time

storage = {
    time.ctime() : {
        "temp": 12,
        "humid": 90
    }
}
print(storage)
time.sleep(1)
storage[time.ctime()] = {
    "temp": 24,
    "humid": 8
}
print(storage)

import json

print(json.dumps(storage))

