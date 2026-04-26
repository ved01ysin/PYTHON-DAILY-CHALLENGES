import random
import copy
import math
import numpy as np
import pandas as pd

def generate_data():
    data = []
    for i in range(12):
        data.append({
            "id": i+1,
            "marks": random.randint(40, 100),
            "attendance": random.randint(60, 100),
            "scores": [random.randint(10, 25), random.randint(10, 25)]
        })
    return data

def mutate_data(data, roll):
    mod = roll % 3
    for i in range(len(data)):
        if i % 3 == mod:
            data[i]["marks"] += math.sqrt(data[i]["marks"])
            data[i]["scores"][0] += 5
            data[i]["attendance"] -= 2

def to_df(data):
    return pd.DataFrame([{
        "id": d["id"],
        "marks": d["marks"],
        "attendance": d["attendance"],
        "internal": d["scores"][0],
        "assignment": d["scores"][1]
    } for d in data])

def analyze(original, modified):
    orig = np.array([d["marks"] for d in original])
    mod = np.array([d["marks"] for d in modified])

    mean = np.mean(mod)
    median = np.median(mod)
    std = np.std(mod)

    drift = abs(np.mean(orig) - mean)

    manual_mean = sum(mod) / len(mod)

    norm = (mod - np.min(mod)) / (np.max(mod) - np.min(mod))

    return mean, median, std, drift, manual_mean, norm

def check_copy_failure(original, shallow):
    for i in range(len(original)):
        if original[i] != shallow[i]:
            return True
    return False

def classify(drift, threshold, failure):
    if failure:
        return "Copy Failure Detected"
    elif drift < threshold:
        return "Stable Data"
    elif drift < threshold * 2:
        return "Minor Drift"
    else:
        return "Critical Drift"

roll_no = 573

original = generate_data()
shallow = copy.copy(original)
deep = copy.deepcopy(original)

mutate_data(shallow, roll_no)
mutate_data(deep, roll_no)

df_original = to_df(original)
df_shallow = to_df(shallow)
df_deep = to_df(deep)

mean, median, std, drift, manual_mean, norm = analyze(original, deep)

failure = check_copy_failure(original, shallow)

threshold = 5
result = classify(drift, threshold, failure)

print("Original DataFrame:\n", df_original)
print("\nShallow Copy:\n", df_shallow)
print("\nDeep Copy:\n", df_deep)

print("\nMean:", mean)
print("Median:", median)
print("Std Dev:", std)
print("Manual Mean:", manual_mean)

print("\nDrift:", drift)
print("Normalized Marks:", norm)

print("\nTuple:", (mean, drift, std))
print("\nClassification:", result)