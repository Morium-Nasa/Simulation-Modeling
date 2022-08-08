import random


def generate(filename):
    fileHandler = open(f"{filename}.txt", "w")

    for datum in range(40):
        fileHandler.write(f"{round(random.random(), 3)}\n")


if __name__ == '__main__':
    # generate a random number ...
    file = input("File name: ")
    generate(file)
