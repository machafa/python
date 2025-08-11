import threading
import time

x=400
lock=threading.Lock()

def double():
	global x,lock
	lock.acquire() #when the limit is acquired, the function should stop
	while x <2000:
		x*=2
		print(x)
		time.sleep(1)
	print("Reacheded The maximum")
	lock.release #here we lock the function by releasing the acquired lock
	
def half():
	global x,lock
	lock.acquire()
	
	while x>1:
		x/=2
		print(x)
		time.sleep(1)
	print("Reacheded The maximum")
	lock.release
		
t1=threading.Thread(target=half)
t2=threading.Thread(target=double)

t1.start()
t2.start()
