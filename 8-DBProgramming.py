import sqlite3

"""
sqlite: module for sqlite (DB)
connect: connect or create (if dont exist) a DB sqlite
cursor: necessary for navigate DB

pass DB rows as Person Object
"""
class Person:
    def __init__(self, id_number=-1, first="", last="", age=-1):
        self.id_number = id_number
        self.first = first
        self.last = last
        self.age = age
        self.connection = sqlite3.connect('mydata.db')
        self.cursor = self.connection.cursor()

    
    def load_person(self, id_number):
        self.cursor.execute("""
        SELECT * FROM persons
        WHERE id = {}
        """.format(id_number))

        results = self.cursor.fetchone()

        self.id_number = id_number
        self.first = results[1]
        self.last = results[2]
        self.age = results[3]

    def insert_person(self):
        self.cursor.execute("""
        INSERT OR IGNORE INTO persons VALUES ({}, '{}', '{}', {})
        """.format(self.id_number, self.first, self.last, self.age))

        self.connection.commit()
        self.connection.close()


def initialize_db():
    """
    Função inicializa o DB populando com valores, chamar novamente irá popular novamente com os mesmos valores
    """
    connection = sqlite3.connect('mydata.db')

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS persons(
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        age INTEGER
    )
    """)

    cursor.execute("""
    INSERT INTO persons VALUES
    (1, 'Paul','Smith',24),
    (2, 'Mark','Johnson',42),
    (3, 'Anna','Smith',34)
    """)

    cursor.execute("""
    SELECT * FROM persons
    WHERE last_name = "Smith"
    """)

    rows = cursor.fetchall()
    print(rows)

    connection.commit()

"""
DELETAR DB ANTES DE CHAMAR initialize_db()
Verifica se a função load obtem os dados do db
"""
#initialize_db()
#p1 = Person()
#p1.load_person(1)
#print(p1.first)
#print(p1.last)
#print(p1.age)
#print(p1.id_number)

"""
Verifica se a função insert_person()
"""

p1 = Person(7,"Alex", "Robbins", 30)
p1.insert_person()

connection = sqlite3.connect('mydata.db')
cursor = connection.cursor()

cursor.execute("SELECT * FROM persons")
results = cursor.fetchall()
print(results)

connection.close()
