from threading import *
import time 

def task(lock):
    lock.acquire()

    # do some work
    for i in range(5):
        print(current_thread().name)
    time.sleep(3)

    lock.release()

mylock = Lock()

thread1 = Thread(target=task,args=(mylock,),name="thread1")
thread2 = Thread(target=task,args=(mylock,),name="thread2")

thread1.start()
thread2.start()