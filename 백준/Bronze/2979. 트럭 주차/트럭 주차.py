from sys import stdin, stdout


def parking(curTime: int, car: list) -> bool:
    return True if car[0] <= curTime < car[1] else False


def solution():
    a, b, c = map(int, stdin.readline().rstrip().split())
    cars: list = list()
    startTime: int = 101
    FinishTime: int = 0
    for _ in range(3):
        s, f = map(int, stdin.readline().rstrip().split())
        if s < startTime:
            startTime = s
        if f > FinishTime:
            FinishTime = f
        cars.append([s, f])

    a1: int = 0
    b2: int = 0
    c3: int = 0

    for i in range(startTime, FinishTime + 1):
        tmp: list = list()
        carCount: int = 0
        for j in cars:
            if parking(i, j) == True:
                tmp.append(j)
                carCount += 1

        if carCount == 1:
            a1 += 1
        elif carCount == 2:
            b2 += 1
        elif carCount == 3:
            c3 += 1
    stdout.write("%d\n" % (a1 * a + b2 * b * 2 + c3 * c * 3))


if __name__ == "__main__":
    solution()
