import queue

q=queue.PriorityQueue()

q.put((2,"Hello Tester"))
q.put((5,"Ahhh"))
q.put((0,2.0))
q.put((8, True))

while not q.empty():
	print(q.get()[1])
