

def new_decorator(original_func):

    def wrap_func():
        print ("This code will be added before original func needs decoration")
        original_func()
        print ("This code will be added after original func needs decoration")

    return wrap_func

@new_decorator
def func_needs_decorator():
    print ("I want to be decorated!!")

#This is straight forward method to implement decorator
print ("###########################################################################")
print ("without use of @ decorator signature for decorator in python")
print ("###########################################################################")
decorated_func = new_decorator(func_needs_decorator)
decorated_func()

print ("###########################################################################")
print ("use of @ decorator signature for decorator in python")
print ("###########################################################################")
func_needs_decorator()


