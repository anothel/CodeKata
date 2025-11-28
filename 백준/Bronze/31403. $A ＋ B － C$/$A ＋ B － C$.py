from sys import stdin


def solution():
    A = int(stdin.readline().strip())
    B = int(stdin.readline().strip())
    C = int(stdin.readline().strip())

    print(A + B - C)
    str = "%d%d" % (A, B)
    print(int(str) - C)


if __name__ == "__main__":
    solution()
