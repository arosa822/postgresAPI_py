#! /usr/bin/env python3

from datetime import datetime
from api import testConn, push
import random
import time

startTime = time.time()
device = 'dataSim'

def test():
    testConn()
    dt = datetime.utcnow()
    device = "testing" 
    state = random.randint(0,11)
    push(device, dt,state)
    return

def main():
    while True:
        try:
            print("sending data to server...")
            push(device,datetime.utcnow(), random.randint(0,11))
        except:
            print('error pushing data')
            break

        time.sleep(15-((time.time()-startTime) % 15.0))



if __name__ == '__main__':
    main()
