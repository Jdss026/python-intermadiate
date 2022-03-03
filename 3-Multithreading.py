import threading
from time import sleep

def function1():
    for x in range(50):
        print("ONE")

def function2():
    for x in range(50):
        print("TWO")

t1 = threading.Thread(target=function1)
t2 = threading.Thread(target=function2) #2 funções simultaneas
t1.start()
t1.join() # espera t1 finalizar antes de seguir para prox linha
t2.start()