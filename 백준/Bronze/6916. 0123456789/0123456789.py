from sys import stdin, stdout


def printNum(n: int):
    if n == 0:
        stdout.write(" * * *\n")
        stdout.write("*     *\n")
        stdout.write("*     *\n")
        stdout.write("*     *\n")
        stdout.write("\n")
        stdout.write("*     *\n")
        stdout.write("*     *\n")
        stdout.write("*     *\n")
        stdout.write(" * * *\n")
    elif n == 1:
        stdout.write("\n")
        stdout.write("      *\n")
        stdout.write("      *\n")
        stdout.write("      *\n")
        stdout.write("\n")
        stdout.write("      *\n")
        stdout.write("      *\n")
        stdout.write("      *\n")
    elif n == 2:
        stdout.write(" * * *\n")
        stdout.write("      *\n")
        stdout.write("      *\n")
        stdout.write("      *\n")
        stdout.write(" * * *\n")
        stdout.write("*\n")
        stdout.write("*\n")
        stdout.write("*\n")
        stdout.write(" * * *\n")
    elif n == 3:
        stdout.write(" * * *\n")
        stdout.write("      *\n")
        stdout.write("      *\n")
        stdout.write("      *\n")
        stdout.write(" * * *\n")
        stdout.write("      *\n")
        stdout.write("      *\n")
        stdout.write("      *\n")
        stdout.write(" * * *\n")
    elif n == 4:
        stdout.write("\n")
        stdout.write("*     *\n")
        stdout.write("*     *\n")
        stdout.write("*     *\n")
        stdout.write(" * * *\n")
        stdout.write("      *\n")
        stdout.write("      *\n")
        stdout.write("      *\n")
    elif n == 5:
        stdout.write(" * * *\n")
        stdout.write("*\n")
        stdout.write("*\n")
        stdout.write("*\n")
        stdout.write(" * * *\n")
        stdout.write("      *\n")
        stdout.write("      *\n")
        stdout.write("      *\n")
        stdout.write(" * * *\n")
    elif n == 6:
        stdout.write(" * * *\n")
        stdout.write("*\n")
        stdout.write("*\n")
        stdout.write("*\n")
        stdout.write(" * * *\n")
        stdout.write("*     *\n")
        stdout.write("*     *\n")
        stdout.write("*     *\n")
        stdout.write(" * * *\n")
    elif n == 7:
        stdout.write(" * * *\n")
        stdout.write("      *\n")
        stdout.write("      *\n")
        stdout.write("      *\n")
        stdout.write("\n")
        stdout.write("      *\n")
        stdout.write("      *\n")
        stdout.write("      *\n")
    elif n == 8:
        stdout.write(" * * *\n")
        stdout.write("*     *\n")
        stdout.write("*     *\n")
        stdout.write("*     *\n")
        stdout.write(" * * *\n")
        stdout.write("*     *\n")
        stdout.write("*     *\n")
        stdout.write("*     *\n")
        stdout.write(" * * *\n")
    elif n == 9:
        stdout.write(" * * *\n")
        stdout.write("*     *\n")
        stdout.write("*     *\n")
        stdout.write("*     *\n")
        stdout.write(" * * *\n")
        stdout.write("      *\n")
        stdout.write("      *\n")
        stdout.write("      *\n")
        stdout.write(" * * *\n")


def solution():
    nList: list = list(stdin.readline().rstrip())

    for i in range(len(nList)):
        printNum(int(nList[i]))
        if i < len(nList) - 1:
            stdout.write("\n")


if __name__ == "__main__":
    solution()
