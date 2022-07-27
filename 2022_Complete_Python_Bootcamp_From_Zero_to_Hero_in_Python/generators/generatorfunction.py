

def get_range(x):
    for i in range(x):
        yield i

g = get_range(7)
print(next(g))
print(next(g))
print(next(g))

s = "hello"
s_iter = iter(s)
print (next(s_iter))
print (next(s_iter))
print (next(s_iter))
print (next(s_iter))
print (next(s_iter))