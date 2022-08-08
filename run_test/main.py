import math

if __name__ == '__main__':
    # Read the data into a list
    data = open('dataset2.txt', 'r')
    nums = []
    data_list = data.readlines()

    # Convert the list to a list of floats
    for i in data_list:
        nums.append(i)

    totalNum = len(nums)
    runs_list = []
    for ptr in range(totalNum - 1):
        if (nums[ptr + 1] - nums[ptr]) < 0:
            runs_list.append('-')
        else:
            runs_list.append('+')

    totalRun = 1
    for ptr in range(len(runs_list) - 1):
        if runs_list[ptr + 1] != runs_list[ptr]:
            totalRun += 1

    print(runs_list)
    print(totalRun)

    miuA = (2 * totalNum - 1) / 3
    sigmaA = math.sqrt((16 * totalNum - 29) / 90)
    z0 = (totalRun - miuA) / sigmaA

    print(f'miuA = {miuA}\nsigmaA = {sigmaA}\nz0 = {z0}')

    zAlphaBy2 = float(input("Enter the value of Z alpha by two: "))

    if z0 >= -zAlphaBy2 or z0 <= zAlphaBy2:
        print("The test is accepted!...")
    else:
        print("Test declined!...")
