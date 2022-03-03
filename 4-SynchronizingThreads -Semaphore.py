from multiprocessing import BoundedSemaphore
from os import access
import threading
import time

#limita o numero de acessos em uma thread com semaphore

semaphore = threading.BoundedSemaphore(value=5)

#função de acesso para um numero predeterminado de threads
def access(thread_number):
    print("{} is trying to access!".format(thread_number))
    semaphore.acquire()
    print("{} is granted access!".format(thread_number))
    time.sleep(5)
    print("{} is now releasing!".format(thread_number))
    semaphore.release()

for thread_number in range(1,11):
    #aciona um numero predeterminado
    t = threading.Thread(target=access, args=(thread_number,))
    t.start() 
    time.sleep(1)
