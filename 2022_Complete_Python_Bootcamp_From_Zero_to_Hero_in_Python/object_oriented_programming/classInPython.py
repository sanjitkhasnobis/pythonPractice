
class test:

    def __init__(self,age,country):
        self.age = age
        self.country = country

    def print_age_country(self):
        print ("Your age is  " + str(self.age))
        print ("Your country is " + str(self.country))


my_test = test(30,'India')
print (type(my_test))
my_test.print_age_country()
