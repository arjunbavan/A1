n=int(input("new loaves bread price: "))
old=n*60/100
a=int(input("enter the number of fresh loaves purchased:"))
b=int(input("enter the number of old loaves purchased:"))
c=a*n
d=(n-old)*b
e=d+c
print("total number loaves of bread: ",a+b)
print("total new number loaves of bread: ",c)
print("total old number loaves of bread: ",d)
print("total cost: ",e)
