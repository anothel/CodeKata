from sys import stdin, stdout


def solution():
    nList: list = list(stdin.readline().rstrip())

    if nList[0] == nList[1]:
        stdout.write("1\n")
    else:
        stdout.write("0\n")


if __name__ == "__main__":
    solution()
