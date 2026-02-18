#program to verify whether three angles can form a triangle or not 
#input of three angles
angle1=float(input("Enter first angle"))
if(angle1<=0):
     print("Invalid angle")
     exit()
else:
    angle2=float(input("Enter second angle"))
    if(angle2<=0):
        print("Invalid angle")
        exit()
    else:
        angle3=int(input("Enter third angle"))
        print("Invalid angle")
        exit()
if (angle1+angle2+angle3)==180:
    print("Valid Triangle")
else:
    print("Invalid Triangle")
    
