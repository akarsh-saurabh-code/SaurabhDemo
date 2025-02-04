import re
name=input("enter name: ")
title=input("enter title: ")
full_name=name +"   "+title
age=(input("enter age: "))
mob=input("enter mobile number")


email=input("enter eamil ID")
country=input("enter country")
state=input("enter state")
city=input("enter city")
town=input("enter town")
house_no=input("enter house number")
address=house_no +" "+ town +" "+ city +" "+ state +" "+ country 
print("Name:" +full_name)
print("Age: " +age)
if mob.isdigit()and len(mob)==10:
    print("Mobile Number: ""+91" +mob)
else:
    print("enter again")
pattern=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-.]+$'
if re.match(pattern,email):
    print("Email: " +email)
else:
    print("invalid")
    email=input("enter eamil ID")       
    if re.match(pattern,email):
        print("Email: " +email)
    else:
        print("invalid")



print("Address: " +address)
#print("Mobile Number: ""+91" +mob)
