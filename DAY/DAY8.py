import random
import math
import numpy as np
import pandas as pd

def generate_data(total_students):
    records=[]
    for i in range(total_students):
        student_id=f"STU{i+1}"
        marks=random.randint(0,100)
        attendance=random.randint(0,100)
        assignment=random.randint(0,50)
        performance_index=(marks*0.6+assignment*0.4)*math.log(attendance+1)
        records.append((student_id,marks,attendance,assignment,performance_index))
    return records

def classify_students(records):
    result={"At Risk":[],"Average":[],"Good":[],"Top Performer":[]}
    for r in records:
        student_id,marks,attendance,_,_=r
        if marks<40 or attendance<50:
            result["At Risk"].append(student_id)
        elif 40<=marks<=70:
            result["Average"].append(student_id)
        elif 71<=marks<=90:
            result["Good"].append(student_id)
        elif marks>90 and attendance>80:
            result["Top Performer"].append(student_id)
    return result

def analyze_data(df):
    marks=df["Marks"].values
    mean=sum(marks)/len(marks)
    median=np.median(marks)
    std=np.std(marks)
    correlation=np.corrcoef(df["Marks"],df["Attendance"])[0][1]
    min_m=min(marks)
    max_m=max(marks)
    df["Normalized Marks"]=[(m-min_m)/(max_m-min_m) if max_m!=min_m else 0 for m in marks]
    consistent=std<15
    low_att=len(df[df["Attendance"]<50])>3
    top=len(df[(df["Marks"]>90)&(df["Attendance"]>80)])>=2
    if consistent and top:
        insight="Stable Academic System"
    elif low_att:
        insight="Critical Attention Required"
    else:
        insight="Moderate Performance"
    summary=(mean,std,max_m)
    return mean,median,std,correlation,summary,insight

roll_last_digit=3
student_count=max(roll_last_digit,10)

student_records=generate_data(student_count)

df=pd.DataFrame(student_records,columns=["Student_ID","Marks","Attendance","Assignment","Performance_Index"])

categories=classify_students(student_records)

unique_students=set([s[0] for s in student_records])

mean,median,std,correlation,summary,insight=analyze_data(df)

print("\nStudent Data:")
print(df.to_string(index=False))

print("\nStudent Categories:")
for k,v in categories.items():
    print(k,":",v)

print("\nStatistics:")
print("Mean:",round(mean,2))
print("Median:",round(median,2))
print("Std Dev:",round(std,2))
print("Correlation:",round(correlation,2))

print("\nSummary Tuple:")
print(summary)

print("\nUnique Student IDs (Set):")
print(unique_students)

print("\nFinal Insight:")
print(insight)