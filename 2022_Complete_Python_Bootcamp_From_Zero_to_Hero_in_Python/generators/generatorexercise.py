import random

def gen_get_squares(n):
   for i in range(n):
        yield i**2

for i in gen_get_squares(10):
    print (i)

g1 = gen_get_squares(10)
next(g1)
next(g1)
next(g1)
next(g1)
next(g1)
next(g1)
next(g1)
next(g1)
next(g1)
next(g1)


#generate n random number between low and high numbers
def get_randomnos(low,high,n):
    for i in range(n):
        yield random.randint(low,high)

print ("Random numbers are getting generated")
for i in get_randomnos(1,10,10):
    print (i)