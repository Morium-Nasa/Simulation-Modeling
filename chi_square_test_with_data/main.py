# Press the green button in the gutter to run the script.
import math
import calculateChiTest as chi

if __name__ == '__main__':
    # Read the data into a list
    data = open('Chi_square_test1.txt', 'r')
    nums = []
    data_list = data.readlines()

    # Convert the list to a list of floats
    for i in data_list:
        nums.append(float(i))

    totalData = len(nums)
    totalClass = round(math.log(totalData) / math.log(2))
    print("Total class: ", totalClass)

    rangeValue = round((max(nums) - min(nums)) / totalClass, 3)
    print("Range difference: ", rangeValue)

    # calculate all classes ranges
    classRanges = {}
    firstStart = min(nums)
    firstEnd = round(firstStart + rangeValue, 3)

    classStart = [firstStart]
    classEnd = [firstEnd]

    for ptr in range(1, totalClass + 1):
        classStart.append(firstEnd)
        firstEnd += rangeValue
        firstEnd = round(firstEnd, 3)
        classEnd.append(firstEnd)

    classRanges = {'start': classStart, 'end': classEnd}

    flag = 0
    oiList = []

    # calculate oi for each class
    print()
    print("Class \t\t   | \tOi")
    print("_______________|_____________")
    for start in classRanges['start']:
        oi = 0
        for ptr in range(totalData):
            if start <= nums[ptr] < classRanges['end'][flag]:
                oi += 1
        print(f"{start} - {classRanges['end'][flag]}  | {oi}")
        oiList.append(oi)
        flag += 1

    # calculate chi square
    # print("Sum of Oi list", sum(oiList))
    print()
    chi.chiTest(oiList, totalClass)
