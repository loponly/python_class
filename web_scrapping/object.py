# class - > object hun - >  Bob, JOhn hun = gar , hul, us, ...
# Dunder methods


import abc


class Person():

    def __init__(self, name, surname):
        print(f'{name} is born')
        self.name = name
        self.surname = surname

    def walk(self):
        print(f'{self.name} walking')

    def run(self):
        self.walk()
        print(f'{self.name} running')

    def __del__(self):
        print(f'{self.name} is deleting')

    def __str__(self):
        return f'Hello {self.name}'

    def __iter__(self):
        pass


# sara.run()
# print(Bob)

# all_person = [Bob, JOhn]

# for person in all_person:
#     person.run()


class Animal():

    def __init__(self, type_):
        self.type_ = type_

    def eat(self):
        print(f'{self.type_} is eating')

    def sleep(self):
        print(f'{self.type_} is sleeping')

    @abc.abstractclassmethod
    def do_something(self):
        pass


class Bird(Animal):

    def __init__(self, name):
        super().__init__('Bird')
        self.name = name

    def fly(self):
        print(f'{self.name} is flying')

    def swim(self):
        print(f'{self.name} is swiming')

    def do_something(self):
        self.eat()
        self.fly()


class Dog(Animal):
    def __init__(self, name):
        super().__init__('Dog')
        self.name = name

    def run(self):
        print(f'{self.name} is running')

    def walk(self):
        print(f'{self.name} is walking')

    def do_something(self):
        self.eat()
        self.run()


class Monkey(Animal):
    def __init__(self, name):
        super().__init__('Monkey')
        self.name = name

    def climb(self):
        print(f'{self.name} is climb')

    def do_something(self):
        self.eat()
        self.climb()


Lucky = Dog('Lucky')
Rio = Bird('Rio')

for animal in [Bird('Rio'), Dog('Lucky'), Monkey('Monkey')]:
    animal.do_something()
