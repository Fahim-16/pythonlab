class rectangle():
 __length=None
 __width=None
 def __init__(self):
    self.__length=int(input("Enter the length:"))
    self.__width=int(input("enter your width:"))
 def area(self):
    return(self.__length*self.__width)
r1=rectangle()
r2=rectangle()
print("Area of Rectangle=",r1.area())
print("Area of Rectangle=",r2.area())
if r1.area()<r2.area():
 print("area2 is greater")
else:
 print("area1 is greater")