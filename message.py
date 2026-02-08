p1 = "Buy now"
p2 = "Subscribe "
p3 = "Make a lot of money"
p4 = "Click here"
message = input("Enter any message : ")
if((p1 in message ) or (p2 in message) or (p3 in message)or(p4 in message)):
    print("This is a Spam :")
else:
    print ("This is  not a spam : ")    