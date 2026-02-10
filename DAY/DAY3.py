n=int(input("Enter number of students:"))
marks=[0]*n
countvalid=0
countfail=0
registerno_last_two_digits=73

for i in range(n):
    marks[i]=int(input("Enter your marks:"))

for i in range(n):
    if marks[i]<0 or marks[i]>100:
        print(marks[i],"Invalid")
    elif marks[i]==registerno_last_two_digits:
        print(marks[i]+27,"Personal case - Excellent")
        countvalid+=1
    elif marks[i]>=90:
        print(marks[i],"Excellent")
        countvalid+=1
    elif marks[i]>=75:
        print(marks[i],"Very Good")
        countvalid+=1
    elif marks[i]>=60:
        print(marks[i],"Good")
        countvalid+=1
    elif marks[i]>=40:
        print(marks[i],"Average")
        countvalid+=1
    else:
        print(marks[i],"Fail")
        countvalid+=1
        countfail+=1

print("Total Valid Students:",countvalid)
print("Total Failed Students:",countfail)
