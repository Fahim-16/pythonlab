#a
list1=[1,2,-3,4,-5,-6,]
print("The list is ",list1)
pnum=list(filter(lambda x:x>0,list1))
print(pnum)

'''lst=[-1,-2,-3,-4,-5,6,7,8,9]
print("the list is ",lst)
nnum=list(filter(lambda x:x<0,lst))
print(nnum)'''

#b
a=[1,2,3,4,5]
b=[a**2 for a in a]
print(b)

#c
input_string = input('enter a string')
input_string = input_string.casefold()
vowels = "aeiou"
data = {}.fromkeys(vowels, 0)
for charecter in input_string:
    if charecter in vowels:
        data[charecter] += 1
for vowel in data:
    print(vowel, "=>", data[vowel])


#d
text=input("Enter the text")
for i in text:
    print(i,"=>",ord(i))