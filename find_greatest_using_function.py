def greatest():
    if(n1>n2 and n1>n3):
        print("n1 is greatest number: " , n1)
    elif(n2>n1 and n2>n3):
        print("n2 is greatest number: " , n2)
    else:
        print("n3 is greatest number: " , n3)       

n1=int(input("Enter 1st number"))
n2=int(input("Enter 2st number"))
n3=int(input("Enter 3st number"))
greatest()        
