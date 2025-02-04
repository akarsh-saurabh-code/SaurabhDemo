#testing email
import re
email=input("enter eami")
pattern=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-.]+$'
if re.match(pattern,email):
    print("Email: " +email)
else:
    print("invalid")
    email=input("enter eamil ID")
    if re.match(pattern,email):
      print("Email: " +email)
    else:
          print("enter again")
          pattern=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-.]+$'
          if re.match(pattern,email):
              print("Email: " +email)
          else:
              print("invalid")