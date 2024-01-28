from graphics.rectangle import*
from graphics.circle import*
from graphics.tdgraphics.sphere import*
from graphics.tdgraphics.cuboid import*
print("Select operation.")
print("1.Rectangle")
print("2.Circle")
print("3.Sphere")
print("4.Cuboid")
while True:
 choice = input("Enter choice(1/2/3/4): ")
 if choice in ('1', '2', '3', '4','5'):
    if choice == '1':
        l=int(input("Enter the length of rectangle:"))
        b=int(input("Enter the breadth of rectangle:"))
        print("Area of rectangle=",rectarea(l,b))
        print("Perimeter of rectangle=",rectperi(l,b))
    if choice=='2':
        r=int(input("Enter the radius of circle:"))
        print("Area of circle=",circlearea(r))
        print("Perimeter of circle=",circleperi(r))
    if choice=='3':
        sr=int(input("Enter the radius of sphere:"))
        print("Area of sphere=",spherearea(sr))
        print("Perimeter of sphere=",sphereperi(sr))
    if choice=='4':
        cl=int(input("Enter the length of cuboid:"))
        w=int(input("Enter the width of cuboid:"))
        h=int(input("Enter the height of cuboid:"))
        print("Area of cuboid=",cuboidarea(cl,w,h))
        print("Perimeter of cuboid=",cuboidperi(cl,w,h))
    if choice == '5':
     exit(0)
 else:
    print("Invalid Input")

def circlearea(radius):
 return 3.14*(radius*radius)
def circleperi(radius):
 return 2*3.14*radius
def rectarea(length,breadth):
 return length*breadth
def rectperi(length,breadth):
 return 2*(length+breadth)
def cuboidarea(l,w,h):
 return((2*l*w)+(2*l*h)+(2*h*w))
def cuboidperi(l,w,h):
 return (4*(l+w+h))
def spherearea(r):
 return (4*3.14*r*r)
def sphereperi(r):
 return (1.33*3.14*r*r*r)