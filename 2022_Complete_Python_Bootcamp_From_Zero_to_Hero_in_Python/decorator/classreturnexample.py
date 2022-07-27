
#Return function concept in python
def hello(name="sanjit"):
    print ("This is a hello function")

    def greet():
        print ("This is a greet function inside hello")

    def welcome():
        print ("This is welcome function inside hello")

    if (name=="sanjit"):
        return greet
    else:
        return welcome

    print ("This is the end of hello function")

if __name__ == "__main__":
     print ("#################Example of returning function#############")
     my_new_func = hello()
     my_new_func()

#passing function as first class parameter
def function_to_pass():
    return "I am passed to another function"

def test_passing_function(input_function):
    print("####################Example of passing function##########################")
    print ("I am inside passing function")
    print (str(input_function()))

test_passing_function(function_to_pass)

