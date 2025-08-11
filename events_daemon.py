import threading

event=threading.Event()

def myfunction():
	print("waiting for event to trigger...")
	event.wait()
	print("Performing action XYZ now")
	
t1=threading.Thread(target=myfunction)
t1.start()

x=input("\nDo you want to trigger the event? Y/N  ")
if x=="y":
	event.set()

