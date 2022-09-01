from sys import stdin, stdout


def solution():
    n: int = int(stdin.readline().rstrip())
    numsN: set = set(map(int, stdin.readline().rstrip().split()))
    m: int = int(stdin.readline().rstrip())
    numsM: list = list(map(int, stdin.readline().rstrip().split()))

    for i in numsM:
        if i in numsN:
            stdout.write("1 ")
        else:
            stdout.write("0 ")


if __name__ == "__main__":
    solution()
