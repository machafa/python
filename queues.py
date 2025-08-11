import queue

q=queue.Queue()

numbers=[1,2,3,4,5,6]

for number in numbers:
	q.put(number)
	
print(q.get())
print(q.get())
print(q.get())
print(q.get())
