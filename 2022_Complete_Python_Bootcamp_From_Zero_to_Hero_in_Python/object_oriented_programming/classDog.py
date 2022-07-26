

class Dog():
    species = 'mammal'

    def __init__(self,breed,name,spots):
        self.breed = breed
        self.name  = name
        self.spots = spots

    def bark(self,number):
        print ("WOOF My name is {}'and my number is {}".format(self.name,number))

my_dog = Dog(breed='Lab',name='Sam',spots=False)
print (my_dog.species)
my_dog.bark(10)


