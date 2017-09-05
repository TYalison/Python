import math
class Circle:
    def __init__(self,radius):
        self.r=radius
    def girth(self):
        g=2*math.pi*(self.r)
        return g
    def area(self):
        a=math.pi*(self.r)*(self.r)
        return a
    def cylinderArea(self,h):
        g=Circle.girth(self)
        a=Circle.area(self)
        cA=g*h+2*a
        return cA
    def cylinderVolume(self,h):
        a=Circle.area(self)
        cV=a*h
        return cV

    
