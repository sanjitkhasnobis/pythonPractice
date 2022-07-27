
#generator method 1 at a time
#not loading list in memory
def get_cube(x):

    for i in range(x):
        yield i

for i in get_cube(1000):
    print (i)

#generating list of values
#without generator without yield
def get_cube_list(x):
    list_of_cube = []
    for i in range(x):
        list_of_cube.append(i)

    return list_of_cube

print ("############################################")
print ("Generating list of Values")
print ("##############################################")
#generating values
for i in get_cube_list(2000):
    #print (i)
    pass

#fibonacci sequence
def get_fibonacci(first_no,second_no,n):

    for i in range(n):
        if(i==0):
            yield first_no
        elif(i==1):
            yield  second_no
        else:
            temp = first_no
            first_no = second_no

            second_no = temp + second_no
            yield  second_no


list_of_fibonacci = []
for i in get_fibonacci(1,1,11):
    list_of_fibonacci.append(i)

print (list_of_fibonacci)


def get_fibonacci_alter(n):
    a = 1
    b = 1

    for i in range(n):
        yield a
        a,b = b,a+b

for i in get_fibonacci_alter(7):
    print (i)





