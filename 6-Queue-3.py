import queue

q = queue.PriorityQueue()

# Insere Prioridade, Valor na queue em tuplas
q.put((2, "Hello World"))
q.put((0, 99))
q.put((5, 7.5))
q.put((1, True))

while not q.empty():
    print(q.get())
