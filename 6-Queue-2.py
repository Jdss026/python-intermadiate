import queue
"""
LIFO Queue: Last In First Out Queue
"""

q = queue.LifoQueue()
# Objeto queue LIFO

numbers = [x for x in range(1,8)]

for x in numbers:
    """
    Insere numeros na queue com put()
    """
    q.put(x)

"""
Metodo get() extrai ultimo elemento da queue
"""
print(q.get())

def list_queue(q) -> list:
    """
    Função que lista os elementos da queue
    Os elementos extraídos na ordem que foram 'empilhados'
    """
    elements_queue = []
    for i in range(0, q.qsize()):
        elements_queue.append(q.get())
    return elements_queue

print(list_queue(q))