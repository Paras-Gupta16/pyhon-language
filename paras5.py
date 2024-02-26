# program to determine the greatest number among three
ao=int(input("enter the 1st number:"))
ai=int(input("enter the 2nd number:"))
ap=int(input("enter the 3rd number:"))
if ao>ai:
    if ao>ap:
        print("1st number is the greatest number")
    else:
        print("3rd number is the graetest number")
elif ai>ap:
    print("2nd number is the gratest numnber")
else:
    print("3rd number is the gratest number")