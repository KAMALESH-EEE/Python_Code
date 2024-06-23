import math

class Shape:

    def get_Area(self):
        pass
    def get_Peri(self):
        pass

class Rectangle(Shape):
    def __init__(self,l,b):
        self._Shape='Rectangle'
        self.__l,self.__b=l,b
        self.__Area = self.__b * self.__l
        self.__Peri = 2*(self.__b + self.__l)

    def get_Area(self):
        return self.__Area
    
    def get_Peri(self):
        return self.__Peri
    
class Square(Rectangle):
    def __init__(self,a):
        
        Rectangle.__init__(self,a,a)
        self._Shape='Square'

class Circle(Shape):
    def __init__(self,r):
        self._Shape='Circle'
        self.__r=r
        self.__Area = math.pi * self.__r * self.__r
        self.__Peri = 2*(math.pi * self.__r)

    def get_Area(self):
        return self.__Area.__round__(2)
    
    def get_Peri(self):
        return self.__Peri.__round__(2)
    
Shape = [Rectangle(2,4),Square(4),Circle(5)]

for i in Shape:
    print(i._Shape)
    print(f'Area: {i.get_Area()} Sq')
    print(f'Perimeter: {i.get_Peri()} units')
