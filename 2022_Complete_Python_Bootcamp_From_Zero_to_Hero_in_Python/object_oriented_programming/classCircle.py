
class Circle:
    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius

    def circumfurance(self):
        return (self.pi * self.radius * 2)

myCrircle = Circle(30)
print (myCrircle.pi)
print (myCrircle.radius)
print (str(myCrircle.circumfurance()))