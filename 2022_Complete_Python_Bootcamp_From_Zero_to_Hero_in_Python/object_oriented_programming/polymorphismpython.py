#polymorphisminpython

class Dog():

    def __init__(self):
      pass
    def bark(self):
        print ("I bark WOFF!!")

class Cat():

    def __init__(self):
        pass

    def bark(self):
        print ("I bark MEW!!")

mycat = Cat()
mycat.bark()
mydog = Dog()
mydog.bark()

for pet in (mydog,mycat):
    print(type(pet))
    pet.bark()

if __name__ == "__main__":
    print ("::::Coming from main method::::")
    mycat1 = Cat()
    mydog1 = Dog()

    def call_pet(pet):
        pet.bark()

    call_pet(mydog1)
    call_pet(mycat1)