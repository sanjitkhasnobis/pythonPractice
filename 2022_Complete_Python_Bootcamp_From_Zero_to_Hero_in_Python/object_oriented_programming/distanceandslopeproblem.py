import math

class calculatepoints:

    def __init__(self,coordinate1,coordinate2):
        self.coordinate1 = coordinate1
        self.coordinate2 = coordinate2

    def calculate_distance(self):
        return (math.sqrt( ((self.coordinate2[1]-self.coordinate1[1])**2) + ((self.coordinate2[0]-self.coordinate1[0])**2) ))

    def calculate_slope(self):
        return (self.coordinate2[1]-self.coordinate1[1])/(self.coordinate2[0]-self.coordinate1[0])

#volume and surface area of cylinder
class volume_and_surfacearea():

    pi = 3.14

    def __init__(self,height,radius):
        self.height = height
        self.radius = radius

    def calculate_volume(self):
        return self.pi*(self.radius**2)*(self.height)

    def calculate_surfacearea(self):
        return 2*(self.pi*(self.radius**2)) + 2*(self.pi*self.radius*self.height)



mycalculatepoints = calculatepoints((30,40),(50,60))
print (str(mycalculatepoints.calculate_distance()))
print (str(mycalculatepoints.calculate_slope()))

myvolume_and_surfacearea = volume_and_surfacearea(30,40)
print (myvolume_and_surfacearea.calculate_surfacearea())
print (myvolume_and_surfacearea.calculate_volume())