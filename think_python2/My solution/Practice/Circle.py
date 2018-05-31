# Circle
# import sys

    
class Point(object):
    count = 0

    @staticmethod
    def status():
        print("total point is:",Point.count)
        
    def __init__(self,name,x,y):
        self.__name = name
        self.x= x
        self.__y= y
        Point.count += 1
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,new_name):
        if new_name == "":
            print("enter something!!!")
        else:
            self.__name = new_name
            print("name change successful.")
    def talk(self):
        print("I am ",self.name)
        
    
        
    def __str__(self):
        print("Name is :",self.name,"x point is :",self.x,"y point is:",self.__y)
        
    def print(self):
        print("the point")
        print(self.x,self.__y)
    def __private_point(self):
        print("as I said it's private", (self.x,self.__y))
    def public_point(self):
        print("I am public",(self.x,self.__y))
        self.__private_point()

    
print(Point.count)   
blank = Point("blank","150","100")
center = Point("center","2","2")


blank.print()
center.print()

print(blank._Point__y)
print(center.x)

try:
    print(center._Point__y)
except AttributeError:
   print("ohoh")
blank.public_point()
center.public_point()

print(center.x)
print(blank._Point__y)
try:
    print(center)
except TypeError:
    False
try:   
    print(blank)
except TypeError:
    None
Point.status()
print (blank.count)
print (center.count)

center.talk()
blank.name = "surface"
blank.talk()
center.name = ""
center.talk()


