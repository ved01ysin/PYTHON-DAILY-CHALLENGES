name= input("Full Name: ")
email= input("Email: ")
mobile= input("Mobile: ")
age= int(input("Age: "))

nameisvalid= True
if name[0]== " " or name[len(name) - 1]== " ":
    nameisvalid = False
elif name.count(" ") < 1:
    nameisvalid = False

emailisvalid= True
if email.count("@")!= 1 or email.count(".")< 1:
    emailisvalid = False
elif email[0]== "@":
    emailisvalid = False

mobileisvalid= True
if len(mobile)!= 10:
    mobileisvalid = False
elif mobile.isdigit()== False:
    mobileisvalid = False
elif mobile[0]== "0":
    mobileisvalid = False

ageisvalid = True
if age>=18 and age<=60:
    ageisvalid = True
else:
    ageisvalid = False

if nameisvalid and emailisvalid and mobileisvalid and ageisvalid:
    print("User Profile is VALID")
else:
    print("User Profile is INVALID")
