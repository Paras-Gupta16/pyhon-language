#program to calculate the sum of a given range between two factors
import math
def common_factor(n1,n2):
    return abs(n1*n2)//math.gcd(n1,n2)
def factor(k,n):
    m=(n-1)//k
    return k*m*(m+1)//2
    return m
def sum_(a,n1,n2):
    f=common_factor(n1,n2)
    s=factor(n1,a)+factor(n2,a)-factor(f,a)
    print(s)
a=int(input("enter the range:"))
n1=int(input("enter the first factor:"))
n2=int(input("enter the second factor:"))
sum_(a,n1,n2)