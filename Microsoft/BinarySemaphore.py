from threading import Thread
from time import sleep

flag = [False,False]
turn = 0



def function(index):
    while True:
        print flag,turn,id(flag)
        choice = raw_input("Thread " + str(index) + " : Do you wanna go inside critical section Y/N : ")
        if choice == "Y":
            common(index)
        else:
            break
        
        
        
    
    
def common(index):
    flag[index] = True
    turn = 1 - index
    while flag[1 - index] and turn == (1 - index):
        print "Thread" + str(index) + " I am waiting. "
    
    print "____________________________________________"
    # critical section
    print "Thread" + str(index) + " I am in critical section. "
    #print flag,turn,id(flag)
    sleep(5)
    print "____________________________________________"
    flag[index] = False
    
    print "Thread" + str(index) + " Remainder section. "
    
    
    
t1 = Thread(target = function,args = (0,))
t2 = Thread(target = function,args = (1,))
t1.start()
t2.start()
    
    
    
    





