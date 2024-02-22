# program to store odd and even number in different list using for loop
a=int(input("enter the starting range:"))
b=int(input("enter the end range:"))
eve=[]
odd=[]
for i in range(a,b):
    if i%2==0:
        eve.append(i)
    else:
        odd.append(i)
print("even list =",eve)
print("odd list =",odd)