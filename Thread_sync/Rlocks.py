# can acquire and release multiple times
# hold info about current thread

from threading import *

# mylock = RLock()
# class BusManager:
#     def __init__(self,available_seats,lock):
#         self.available_seats = available_seats
#         self.lock = lock
        

#     # shared resources
#     def reserve(self,needed_seats):
#         self.lock.acquire()  # acquire the lock before accessing shared resource
#         self.lock.acquire()  # acquire the lock before accessing shared resource
#         print(self.lock)
#         print(f"available_seats are {self.available_seats}")
#         if self.available_seats >= needed_seats:
#             user = current_thread().name
#             # mimicking the DB updation
#             self.available_seats -= needed_seats
#             print(f"{needed_seats} are allocated to user {user}")
#         else:
#             print("Not enough seats available.")


#         self.lock.release()
#         self.lock.release()

# # total number of seats are 2
# b1 = BusManager(2,mylock)

# # creating threads that will execute simultaneously
# # both user need 1 seats
# t1 = Thread(target=b1.reserve, args=(2,), name="user1")
# t2 = Thread(target=b1.reserve, args=(1,), name="user2")
# t1.start()
# t2.start()


l = RLock()
def get_first_line():
    l.acquire()
    print(f"Thread {current_thread().name} got the lock")
    l.release()
    print(f"Thread {current_thread().name} release the lock")


def get_last_line():
    l.acquire()
    print(f"Thread {current_thread().name} got the lock")
    l.release()
    print(f"Thread {current_thread().name} release the lock")

def main():
    l.acquire()
    get_first_line()
    get_last_line()
    l.release()

t1 = Thread(target=main)
t1.start()