class Person:
    amount = 0 #variavel da classe

    def __init__(self,name, age, height):
        self.name = name
        self.age = age
        self.height = height
        Person.amount+=1 # referencia a classe e nao o objeto (self)

    def __del__(self): # metodo para deletar objeto
        Person.amount -= 1
        print("Pessoa Deletado: {}".format(self.name))

    def __str__(self): # metodo para print objeto
        return("Name: {}, Age: {}, Height: {}".format(self.name, self.age, self.height))

    def get_older(self, years):
        self.age += years

person1 = Person("Mike",30,180)
print(person1)

print(Person.amount)

person2 = Person("Ana",35,160)
print(person2)

print(Person.amount)

person2.get_older(2)

print(person2)