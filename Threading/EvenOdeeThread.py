import threading
from math import ceil
from random import random
from Queue import Queue
from threading import Lock

count = 0
lock = Lock()

class Odd(threading.Thread):
    def __init__(self, name, size, objQueue):
        threading.Thread.__init__(self, name=name)
        self.size = size
        self.objQueue = objQueue
    
    def run(self):
        global count
        global lock
        p = 0
        
        while p < self.size:
            lock.acquire()
            if count % 2 == 1:
                print "Odd" , count
                count += 1
                p += 1
            lock.release()
            
            
            
class Even(threading.Thread):
    def __init__(self, name, size, objQueue):
        threading.Thread.__init__(self, name=name)
        self.size = size
        self.objQueue = objQueue
    
    def run(self):
        global count
        global lock
        p = 0
        
        while p < self.size:
            lock.acquire()
            if count % 2 == 0:
                print "Even" , count
                count += 1
                p += 1
            lock.release()
            
            
class Threading(object):
    def runThreads(self):
        objQueue = Queue(20)
        
        odd = Odd('Thread-Odd', 10, objQueue)
        even = Even('Thread-Even', 10, objQueue)
        threads = []
        threads.append(odd)
        threads.append(even)
        
        odd.start()
        even.start()
        
        for thread in threads:
            thread.join()
            print(thread.name + " done")
        print("All threads done")

        while not objQueue.empty():
            print(objQueue.get())
        
if __name__ == "__main__":
    objThreading = Threading()
    objThreading.runThreads()