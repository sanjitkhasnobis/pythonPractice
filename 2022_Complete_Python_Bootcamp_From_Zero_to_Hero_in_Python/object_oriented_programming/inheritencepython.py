#inheritence in python

class Animal():

    def __init__(self):
        print ("I am in Animal")

    def eat(self):
        print ("I love to eat burgers")

    def bark(self):
        print ("I bark less")

class Dog(Animal):


    def __init__(self):
        Animal.__init__(self)
        print ("I am in Dog")

myDog = Dog()
myDog.eat()
myDog.bark()

