transactions=[]
s=input("Enter transactions: ")
num=""

for ch in s:
    if ch!=" ":
        num+=ch
    else:
        if num!="":
            transactions.append(int(num))
            num=""
            
if num!="":
    transactions.append(int(num))
categories={"normal":[],"large":[],"high_risk":[],"invalid":[]}

for t in transactions:
    if t<=0:
        categories["invalid"].append(t)
    elif t<=500:
        categories["normal"].append(t)
    elif t<=2000:
        categories["large"].append(t)
    else:
        categories["high_risk"].append(t)
        
valid=[t for t in transactions if t>0]
total=sum(valid)
count=len(valid)
summary=(total,count)
freq=False

if count>5:
    freq=True
large_spend=False

if total>5000:
    large_spend=True
suspicious=False

if len(categories["high_risk"])>=3:
    suspicious=True
true_count=0

if freq:
    true_count+=1
    
if large_spend:
    true_count+=1
    
if suspicious:
    true_count+=1
    
if true_count==0:
    risk="Low Risk"
    
elif true_count==1:
    risk="Moderate Risk"
    
else:
    risk="High Risk"
    
print("Categorized Transactions:",categories)
print("Total Transaction Value:",summary[0])
print("Number of Transactions:",summary[1])
print("Final Risk Classification:",risk)