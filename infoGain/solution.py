import pandas
import math

# GETTING THE DATA
data = pandas.read_csv('prlab3dataset.csv')


# CALCULATING THE ENTROPY for the whole data set
def entropy(maleCount, femaleCount, totalData):
    if totalData == 0 or maleCount == 0 or femaleCount == 0:
        return 0
    else:
        return round(-(maleCount / totalData) * (math.log2(maleCount / totalData)) \
                     - (femaleCount / totalData) * (math.log2(femaleCount / totalData)), 4)


# CALCULATING THE ENTROPY attribute wise ...
def atrributeWiseEntropy(attribute, condition):
    yesCount, noCount, yesMaleCount, yesFemaleCount, noMaleCount, noFemaleCount = 0, 0, 0, 0, 0, 0
    for datum in range(totalData):
        if data.iloc[datum][attribute] <= condition:
            yesCount += 1
            if data.iloc[datum]['class'] == 'm':
                yesMaleCount += 1
            elif data.iloc[datum]['class'] == 'f':
                yesFemaleCount += 1
        else:
            noCount += 1
            if data.iloc[datum]['class'] == 'm':
                noMaleCount += 1
            elif data.iloc[datum]['class'] == 'f':
                noFemaleCount += 1

    yesEntropy = entropy(yesMaleCount, yesFemaleCount, yesCount)
    noEntropy = entropy(noMaleCount, noFemaleCount, noCount)

    # CALCULATING THE INFORMATION GAIN, attribute wise ...
    ig = mainEntropy - ((yesCount / totalData) * yesEntropy + (noCount / totalData) * noEntropy)

    resultDict = {'yes': yesEntropy, 'no': noEntropy, 'ig': round(ig, 4)}

    return resultDict


# main function to calculate the information gain
mainEntropy, maleCount, femaleCount = 0, 0, 0
totalData = len(data)

for datum in range(totalData):
    if data.iloc[datum]['class'] == 'm':
        maleCount += 1
    elif data.iloc[datum]['class'] == 'f':
        femaleCount += 1

mainEntropy = entropy(maleCount, femaleCount, totalData)
#print(data)
print("Main Entropy: ", mainEntropy)

# hair length section ...
print()
hairLength = int(input("Enter the hair length <=: "))
hairLengthInfo = atrributeWiseEntropy('hairlength', hairLength)

print("Hair Length Yes Entropy: ", hairLengthInfo['yes'])
print("Hair Length No Entropy: ", hairLengthInfo['no'])
print("Hair Length Information Gain: ", hairLengthInfo['ig'])

# weight section ...
print()
weightValue = int(input("Enter the weight <=: "))
weightInfo = atrributeWiseEntropy('weight', weightValue)

print("Weight Yes Entropy: ", weightInfo['yes'])
print("Weight No Entropy: ", weightInfo['no'])
print("Weight Information Gain: ", weightInfo['ig'])

# Age section ...
print()
age = int(input("Enter the age <=: "))
ageInfo = atrributeWiseEntropy('age', age)

print("Age Yes Entropy: ", ageInfo['yes'])
print("Age No Entropy: ", ageInfo['no'])
print("Age Information Gain: ", ageInfo['ig'])
