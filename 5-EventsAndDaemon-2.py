from concurrent.futures import thread
import threading
import time

# adiciona o caminho do arquivo de texto
path = "text.txt"
text = ""

#realiza a leitura do arquivo quando invocado
def readFile():
    global path, text
    while True:
        with open("text.txt", "r") as f:
            text = f.read()
        #time.sleep(3)

# realiza a impressao das linhas do texto
def printloop():
    x = 0
    while True:
        print("line {}: {}".format(x, text))
        x +=1
        time.sleep(1)

# configurando readFile como daemon (background)
t1 = threading.Thread(target=readFile, daemon=True)
t2 = threading.Thread(target=printloop)

t1.start()
t2.start()