# chi square test inputting directly value of Oi

totalClass = int(input("Enter total class: "))
Oi = []
N = 0
Dobs = 0

for ptr in range(totalClass):
    tempOi = float(input(f"Enter Oi for class no {ptr + 1}: "))
    Oi.append(tempOi)
    N += tempOi

print("All Oi :", Oi)
Ei = N / totalClass

for datum in Oi:
    Dobs += pow((datum - Ei), 2) / Ei

print("D obs is: ", Dobs)

Dcritical = float(input("Enter D critical: "))

if Dobs <= Dcritical:
    print("Test result is Accepted")
else:
    print("Test result is Rejected")
