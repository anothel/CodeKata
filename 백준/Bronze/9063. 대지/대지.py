from sys import stdin, stdout


def solution():
    xList: list = list()
    yList: list = list()
    for _ in range(int(stdin.readline().rstrip())):
        x, y = map(int, stdin.readline().rstrip().split())
        xList.append(x)
        yList.append(y)
    stdout.write("%d\n" % (abs(max(xList) - min(xList)) *
                 abs(max(yList) - min(yList))))


if __name__ == "__main__":
    solution()
