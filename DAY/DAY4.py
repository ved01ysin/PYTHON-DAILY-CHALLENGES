low_risk=[]
medium_risk=[]
high_risk=[]
critical_risk=[]

valid=0
ignore=0
remove=0

D=int(input("Enter last digit of your Registerion Number: "))
n=int(input("Enter number of activity scores: "))

scores=[]

for i in range(n):
    m=int(input("Enter score: "))
    scores=scores+[m]

for i in range(len(scores)):

    if scores[i]<0:
        ignore=ignore+1
    else:
        valid=valid+1
        if scores[i]<=30:
            low_risk=low_risk+[scores[i]]
        elif scores[i]<=60:
            medium_risk=medium_risk+[scores[i]]
        elif scores[i]<=100:
            high_risk=high_risk+[scores[i]]
        else:
            critical_risk=critical_risk+[scores[i]]

print("\nRegister Digit (D):",D)
print("Low Risk:",low_risk)
print("Medium Risk:",medium_risk)
print("High Risk:",high_risk)
print("Critical Risk:",critical_risk)

if D%2==0:
    remove=len(low_risk)
    low_risk=[]
else:
    remove=len(critical_risk)
    critical_risk=[]

print("\nAfter Personalized Filtering:")
print("Low Risk:",low_risk)
print("Medium Risk:",medium_risk)
print("High Risk:",high_risk)
print("Critical Risk:",critical_risk)
print("\nTotal Valid Entries:",valid)
print("Ignored Entries:",ignore)
print("Removed Due to Personalization:",remove)
