#Name:Ojas Joshi
#Gr no:11810839
#roll no:23
#Division:M
def armstrong(n):
    sum=0
    t=n
    while t>0:
        d=t%10
        sum=t**3
        t=t//10
    return sum
n=int(input("Enter a number"))
y=armstrong(n)
print(y)
