#Q1
import threading
import time
class Mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i
    def run (self):

        print("Value read",self.h)
thread1=Mythread(20)
thread1.start()
time.sleep(5)
#Q2
import threading
import time
class Mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i
    def run(self):
            print("No is",self.h)
for i in range(1,11):
    thread1=Mythread(i)
    thread1.start()
    time.sleep(1)

#Q3
import threading
import time
list=[1,3,5,7,10]
class Mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i
    def run(self,counter):
        time.sleep(counter)
        print("The list is:",self.h)
for i in list:
    thread1=Mythread(i)
    thread1.run(i)

#Q4
import threading
import math
class Mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i
    def run(self):
        m=self.h
        f=math.factorial(m)
        print("The Factorial No is",f)
a=int(input("Enter no:"))
thread=Mythread(a)
thread.start() 
