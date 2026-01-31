stuID=input("ID: ")
emailID=input("Email: ")
passw=input("Password: ")
refcode=input("Referral: ")

passwordisvalid=True
if len(passw)<8 or passw[0].isupper()==False:
    passwordisvalid=False
if passw[0].isdigit()==False and passw[1].isdigit()==False and passw[2].isdigit()==False and passw[3].isdigit()==False and passw[4].isdigit()==False and passw[5].isdigit()==False and passw[6].isdigit()==False and passw[7].isdigit()==False:
    passwordisvalid=False



studentisvalid=True
if len(stuID)!=7 or stuID[:3]!="CSE" or stuID[3]!="-" or stuID[4:7].isdigit()==False:
    studentisvalid=False


emailisvalid=True
if "@" not in emailID or "." not in emailID or emailID[0]=="@" or emailID[-1]=="@" or emailID[-4:]!=".edu":
    emailisvalid=False


referralisvalid=True
if len(refcode)!=6 or refcode[:3]!="REF" or refcode[3:5].isdigit()==False or refcode[-1]!="@":
    referralisvalid=False


if passwordisvalid and studentisvalid and emailisvalid and referralisvalid:
    print("APPROVED")
else:
    print("REJECTED")
