print("Hello World")
for i in range(1,10):
    print(i)
    if(i==5):
      break 
a=2
b=20#Assignment Operator
a+=2
print(a)
sum=a+b #Arithmetic Operator
sub=a-b
div=a/b
mul=a*b
mod=a%b

print(sum)
print(sub)
print(div)
print(mul)
print(mod)
#Comparison Operator [<,>,<=,>=,==]
if(a<b): 
   print("a is greater")
else:
   print("b is greater")

#Logical

#and True if both is true
#or True if either is true
#not Complement


x=True
y=False

print('x and y is',x and y)
print('x or y is',x or y)
print('not x is',not x)

#Bitwise
n1=5
n2=6
print(n1|n1)
print(n1 & n2)
print(a^b)
print(n1<<2)
print(n2>>2)


#Membership 
List=[1,23,3,2]
print(21 in List)
print(21 not in List)

#Area of circle
PI=3.14
r=int(input("Enter number:"))
Area=PI*r*r
print("Area of circle:",Area)


#datatypes of python
a=int(input("Enter number:"))
b=int(input("Enter number:"))
sum=a+b
print(type(sum))
c=int(input("Enter number:"))
d=float(input("Enter number:")) 
print(c,d)
sum1=c+d
print(type(sum1))
PLS=231 #constant
print(PLS)