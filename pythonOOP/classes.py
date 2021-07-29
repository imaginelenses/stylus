class Person:
    def __init__(self, name, age, phoneNumber):
        self.name = name
        self.age = age
        self.phoneNumber = phoneNumber

    def greet(self):
        print('Hello, ' + self.name)

