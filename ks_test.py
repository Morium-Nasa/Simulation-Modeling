# chi square test inputting directly value of data

totalClass = int(input("How Many Numbers: "))
data, ratioPlus, ratioMinus, dPlus, dMinus = [], [], [], [], []
Dobs = 0

for ptr in range(totalClass):
    tempdata = float(input(f"Data no {ptr + 1}: "))
    data.append(tempdata)

print("All data :", sorted(data))

for datum in range(totalClass):
    ptr = datum + 1

    ratioPlus.append(float(ptr/totalClass))
    ratioMinus.append(float(datum/totalClass))

    dPlus.append(ratioPlus[datum] - data[datum])
    dMinus.append(data[datum] - ratioMinus[datum])

dPlusMax = max(dPlus)
dMinusMax = max(dMinus)
print(f"D plus max: {dPlusMax}")
print(f"D minus max: {dMinusMax}")

dObs = max(dPlusMax, dMinusMax)
print(f"D obs: {dObs}")

dCritical = float(input("Enter D critical: "))

if dObs <= dCritical:
    print("Test result is Accepted")
else:
    print("Test result is Rejected")
