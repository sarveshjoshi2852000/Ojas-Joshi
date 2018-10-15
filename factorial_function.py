#factorial using functions
#OjasJoshi
#DIvison M

def factorial(x):
   if x<0:
     print("Enter a positive number")
   elif x==0:
       print("Factorial is 1")
   else:
       y=1
       while x>0:
            y=x*y
            x=x-1
       return y
x=int(input())
b=factorial(x)
print(b) 
