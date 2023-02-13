from sys import stdin, stdout


def printNum(n: int):
    if n == 0:
        stdout.write("0000\n")
        stdout.write("0  0\n")
        stdout.write("0  0\n")
        stdout.write("0  0\n")
        stdout.write("0000\n")
    elif n == 1:
        stdout.write("   1\n")
        stdout.write("   1\n")
        stdout.write("   1\n")
        stdout.write("   1\n")
        stdout.write("   1\n")
    elif n == 2:
        stdout.write("2222\n")
        stdout.write("   2\n")
        stdout.write("2222\n")
        stdout.write("2\n")
        stdout.write("2222\n")
    elif n == 3:
        stdout.write("3333\n")
        stdout.write("   3\n")
        stdout.write("3333\n")
        stdout.write("   3\n")
        stdout.write("3333\n")
    elif n == 4:
        stdout.write("4  4\n")
        stdout.write("4  4\n")
        stdout.write("4444\n")
        stdout.write("   4\n")
        stdout.write("   4\n")
    elif n == 5:
        stdout.write("5555\n")
        stdout.write("5\n")
        stdout.write("5555\n")
        stdout.write("   5\n")
        stdout.write("5555\n")
    elif n == 6:
        stdout.write("6666\n")
        stdout.write("6\n")
        stdout.write("6666\n")
        stdout.write("6  6\n")
        stdout.write("6666\n")
    elif n == 7:
        stdout.write("7777\n")
        stdout.write("   7\n")
        stdout.write("   7\n")
        stdout.write("   7\n")
        stdout.write("   7\n")
    elif n == 8:
        stdout.write("8888\n")
        stdout.write("8  8\n")
        stdout.write("8888\n")
        stdout.write("8  8\n")
        stdout.write("8888\n")
    elif n == 9:
        stdout.write("9999\n")
        stdout.write("9  9\n")
        stdout.write("9999\n")
        stdout.write("   9\n")
        stdout.write("   9\n")


def solution():
    nList: list = list(stdin.readline().rstrip())

    for i in range(len(nList)):
        printNum(int(nList[i]))
        if i < len(nList) - 1:
            stdout.write("\n")


if __name__ == "__main__":
    solution()
