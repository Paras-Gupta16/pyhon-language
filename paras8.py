# linear search in python
def linear(a,key):
    for i in  range(len(a)):
        if key==a[i]:
            return i+1
    else:
        return -1
    pass
a=[]
n=int(input("enter the number of element you want to enter:"))
for i in range(n):
    ele=int(input(f"enter the element{i+1}:"))
    a.append(ele)
print("element you enter")
for i in range(n):
    print(a[i],end=" ")
print("\n")
key=int(input("enter the element you want to search:"))
l=linear(a,key)
if l!=-1:
    print("element  founded at postion",l)
else:
    print("element doesn't exists")