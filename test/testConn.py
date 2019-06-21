#! /usr/bin/env python3

from datetime import datetime
from api import testConn, push
import random
import time


def main():
    testConn()
    dt = datetime.utcnow()
    device = "testing" 
    state = random.randint(0,11)
    push(device, dt,state)
    return

if __name__ == '__main__':
    main()
