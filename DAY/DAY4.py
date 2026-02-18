name = input("Enter your full name: ")
L = 0
for i in range(len(name)):
    if name[i] != " ":
        L = L + 1
PLI = L % 3

n = int(input("Enter number of requests: "))
req = []
for i in range(n):
    number = int(input("Enter request value (0 to 50): "))
    req.append(number)

low = []
moderate = []
high = []
invalid = []
valid_req = 0
removed = 0

for i in range(len(req)):
    number = req[i]
    if number < 0:
        invalid.append(number)
    elif number == 0:
        pass
    elif number <= 20:
        low.append(number)
        valid_req = valid_req + 1
    elif number <= 50:
        moderate.append(number)
        valid_req = valid_req + 1
    else:
        high.append(number)
        valid_req = valid_req + 1

if PLI == 0:
    removed = len(low)
    low = []
    print("PLI is", PLI)
    print("Rule A: Removed Low Demand")
elif PLI == 1:
    removed = len(high)
    high = []
    print("PLI is", PLI)
    print("Rule B: Removed High Demand")
else:
    removed = len(low) + len(high)
    low = []
    high = []
    print("PLI is", PLI)
    print("Rule C: Keep Only Moderate Demand")

print("L is", L)
print("Valid requests are", valid_req)
print("Removed requests are", removed)
print("Low Demand:", low)
print("Moderate Demand:", moderate)
print("High Demand:", high)
print("Invalid Requests:", invalid)
