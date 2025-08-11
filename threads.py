import threading

def helloword():
	for x in range (50):
		print("BY3")
def byeword():
	for x in range (50):
		print("H3II0")
ti1=threading.Thread(target=helloword)
ti2=threading.Thread(target=byeword)

ti1.start()
ti2.start()
