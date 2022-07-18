from sys import stdin, stdout


def getDistance(x1: int, y1: int, x2: int, y2: int) -> int:
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5


def solve():
    x_f: int = 0
    y_f: int = 0
    x_b: int = 0
    y_b: int = 0
    answer: int = 0
    for i in range(int(stdin.readline().rstrip())):
        x, y = map(int, stdin.readline().rstrip().split())
        if i == 0:
            x_f = x_b = x
            y_f = y_b = y
            continue
        answer += getDistance(x_b, y_b, x, y)
        x_b = x
        y_b = y

    answer += getDistance(x_b, y_b, x_f, y_f)

    stdout.write("%d\n" % answer)


if __name__ == "__main__":
    solve()
