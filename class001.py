class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def add_prefix(self):
        return 'ok'

    @property
    def displayFullName(self):
        return self.first_name + " " + self.last_name


""" USE CLASS """
emp1 = Employee('Sandra', 'Kuratowski')

print(emp1.first_name)
print(emp1.add_prefix)
print(emp1.displayFullName)
