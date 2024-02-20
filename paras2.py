# how to use for loop
# for example we want to print the table of any number using for loop
a=float(input("enter the number:"))
# enter the start and end range
start=int(input("enter the staring range where you want to print the table:"))
end=int(input("enter the end range of the table:"))
for i in range(start,end+1):
    print(a,"*",i,"=",a*i)
