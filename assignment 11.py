#REGULAR EXPRESSIONS IN PYTHON
#Q.1- Write a python code to find a valid email address from a text.

#Answer:[a-zA-Z0-9_.]*[@](gmail.com|yahoo.com)

import re
email=input("Enter the email address:")
match=re.match('[a-zA-Z0-9_.]*[@](gmail.com|yahoo.com|icloud.com|rediffmail.com|hotmail.com)',email)
if(match!=None):
    print("Valid  Email Address.")
    extract=re.split('@',email)
    print("User name is:",extract[0],"\nDomain name is:",extract[1])
else:
    print("Invalid Email Address.")

#Q.2- Write a python program to find a valid Indian phone number from a text.(Valid Indian numbers will start with "+91-" and after that [6-9] followed by 9 digits. )
    
#Answer: ^+91^[6-9][0-9]{9}      or ^+91^[6789][0-9]{9}      or ^+91^[6-9]\d{9}      or ^+91^[6789]\d{9}

phone=input("Enter a phone number:")
match=re.match('^(\+91-)[6-9]\d{9}',phone)
if(match!=None):
    print("Valid Phone Number.")
    number=re.split('-',phone)
    print("Number is: " , number[1])
else:
    print("Invalid Phone Number.")
