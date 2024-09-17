class employee:

    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def display(self):
        print(f'ID:{self.id} | NAME:{self.name} | SALARY:{self.salary}')

a = employee('1', 'ABC', 1000000)

a.display()