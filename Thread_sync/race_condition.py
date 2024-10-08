'''
A race condition in an operating system happens when the behavior of software depends on the sequence or timing of uncontrollable events like threads or processes executing. When multiple threads access shared resources without proper synchronization, the final outcome can vary, leading to unpredictable bugs. Picture two chefs trying to use the same kitchen without coordinating—might get some weird dishes! Got any more OS-related wonders on your mind?
'''

# bus management system 

from threading import *

class BusManager:
    def __init__(self,available_seats):
        self.available_seats = available_seats
        

    # shared resources
    def reserve(self,needed_seats):
        print(f"available_seats are {self.available_seats}")
        if self.available_seats >= needed_seats:
            user = current_thread().name
            # mimicking the DB updation
            self.available_seats -= needed_seats
            print(f"{needed_seats} are allocated to user {user}")
        else:
            print("Not enough seats available.")


# total number of seats are 2
b1 = BusManager(2)

# creating threads that will execute simultaneously
# both user need 1 seats
t1 = Thread(target=b1.reserve, args=(2,), name="user1")
t2 = Thread(target=b1.reserve, args=(1,), name="user2")
t1.start()
t2.start()