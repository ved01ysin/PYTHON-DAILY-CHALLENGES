import copy

def new_inventory():
    return [
        {
            "item": "Laptop",
            "details": {"price": 50000, "stock": 10, "rating": 4.5}
        },
        {
            "item": "Phone",
            "details": {"price": 20000, "stock": 25, "rating": 4.2}
        },
        {
            "item": "Tablet",
            "details": {"price": 30000, "stock": 15, "rating": 4.8}
        }
    ]

def apply_mutation(data, roll_number):
    target = roll_number % len(data)
    
    for i in range(len(data)):
        if i == target:
            data[i]["details"]["price"] = int(data[i]["details"]["price"] * 0.9)
            data[i]["details"]["stock"] -= 5
            data[i]["item"] = data[i]["item"] + " (Modified)"

def compare_data(original, shallow, deep):
    changed = 0
    unchanged = 0
    
    print("\n--- Comparative Analysis ---")
    for i in range(len(original)):
        if original[i]["details"]["price"] != deep[i]["details"]["price"]:
            print(f"Item {i}: Original DATA CORRUPTED by Shallow Copy mutation!")
            changed += 1
        else:
            print(f"Item {i}: Original data remains isolated.")
            unchanged += 1
            
    return (changed, unchanged)

roll_no = 573

original = new_inventory()
shallow = copy.copy(original) 
deep = copy.deepcopy(original)

apply_mutation(shallow, roll_no)

print(f"Original Inventory:\n{original}")
print(f"\nShallow Copy Result (Mutated):\n{shallow}")
print(f"\nDeep Copy Result (Isolated):\n{deep}")

summary = compare_data(original, shallow, deep)

print(f"\nSummary Tuple (Changed, Unchanged): {summary}")