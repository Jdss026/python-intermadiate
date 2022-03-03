class Person:
    def __init__(self,name, age, height):
        self.name = name
        self.age = age
        self.height = height
        
    def __str__(self): # metodo para print objeto
        return "Name: {}, Age: {}, Height: {}".format(self.name, self.age, self.height)

    def get_older(self, years):
        self.age += years

class Worker(Person): # Worker herda os métodos de Person
    def __init__(self, name, age, height, salary):
        #super herda o metodo init, adiciona salary
        super(Worker, self).__init__(name, age, height)
        self.salary = salary

    def __str__(self):
        text = super(Worker, self).__str__()
        text += ", Salary: {}".format(self.salary)
        return text

    def calc_year_salary(self):
        return self.salary*12

class Vector: #operator overlead
    def __init__(self,x,y):
        self.x = x 
        self.y = y

    def __add__(self, other): #metodo de soma de objetos
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other): #metodo de subtração de objetos
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self): #define print do objeto
        return "X: {}, Y: {}".format(self.x, self.y)

if __name__=='__main__':
    worker1 = Worker("Henry", 40, 176, 3000)
    print(worker1)
    print(worker1.calc_year_salary())

    # operacoes com vetores

    v1 = Vector(2,3)
    v2 = Vector(4,5)

    print(v1)
    print(v2)

    v3 = v1-v2

    print(v3)