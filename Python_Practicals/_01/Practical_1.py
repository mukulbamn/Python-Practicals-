print("Program to calculate the area and perimeter of a triangle !")
ch="Y"
while ch=="Y" or ch=="y":
    a,b,c=map(int, input("Enter 3 sides : ").split())
    if a+b<=c or a+c<=b or b+c<=a:
        print("Not a Triangle, because the sum of two any sides must be greater than the third ! ")
        
    else :
        
        s=(a+b+c)/2
        t=((s*(s-a)*(s-b)*(s-c))**0.5,(a+b+c))
        print("","AREA :",t[0],"\nPERIMETER :",t[1])
    ch=input("Do you want to continue ? \n(Y)es or (N)o\n")
