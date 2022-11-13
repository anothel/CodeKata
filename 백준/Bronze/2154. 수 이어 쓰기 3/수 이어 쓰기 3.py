from sys import stdin, stdout


def solution():
    curStr: str = ''
    n: str = stdin.readline().rstrip()

    for i in range(1, 100001):
        curStr += str(i)

    stdout.write("%d\n" % (curStr.index(n) + 1))


if __name__ == "__main__":
    solution()