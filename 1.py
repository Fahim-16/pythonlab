a=int(input("Enter the starting value:"))
b=int(input("enter the ending value:"))
for i in range(a,b):
    if (0==i%4)and (0!=i%100)or(0==1%400):
        print(i)