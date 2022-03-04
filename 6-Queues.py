import queue

"""
Working with queues
LIFO: Last In First Out Queue
"""

q = queue.Queue()

numbers = [10, 20, 30, 40, 50, 60, 70]
for number in numbers:
    q.put(number)

print(q.get())
print(q.get())

elements_queue = [] 

def list_queue(q) -> list:
    for i in range(0, q.qsize()):
        elements_queue.append(q.get())
    return elements_queue

print(list_queue(q))