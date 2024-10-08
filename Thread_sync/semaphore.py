# semaphors used to limit the access to the shared resource with limited capacity
# maintains counter which represents the number of threads can access the shared resource
# acuire reduces the counter (if 0 means no more threads can access the shared resource)
# releases increases the counter 

from threading import *
import time

# semaphore
# default value is 1 
obj = Semaphore(2)

def displayThread(name):
    obj.acquire()
    # doing something
    for i in range(5):
        print(f"{name} is running")
        time.sleep(.5)
    obj.release()


t1 = Thread(target=displayThread, args=("Thread 1",))
t2 = Thread(target=displayThread, args=("Thread 2",))
t3 = Thread(target=displayThread, args=("Thread 3",))
t4 = Thread(target=displayThread, args=("Thread 4",))
t1.start()
t2.start()
t3.start()
t4.start()

