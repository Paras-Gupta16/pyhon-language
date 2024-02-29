#program to use the dictionary
#so dictionary has key : value pair
d={}
a=int(input("enter the number of student you want to enter the detail:"))
for i in range(a):
    b=input("enter the name of the student:")
    c=int(input("enter the marks of the student:"))
    d[b]=c
# now print the dictionary
print("dictionary=",d)