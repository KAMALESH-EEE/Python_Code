import threading
import time
num = list(range(1,1001,1))
num1 = list(range(1,1001,1))
print(num)

def sq(num):
    for i in num:
        print('Square:',i,'is',i**2)
def cu(num):
    for i in num:
        print('cube:',i,'is',i**3)

t1 = threading.Thread(target=sq,args=(num,))
t2 = threading.Thread(target=cu,args=(num1,))
ts = time.time_ns()
t1.start()
t2.start()
t1.join()
t2.join()
te = time.time_ns()
print("Total Exicution time: ",(te-ts)/10000,'uS')
print(__file__)