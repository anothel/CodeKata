from sys import stdin, stdout


def getAnswer(w: int, m: int) -> float:
    sum_m: int = m * 10
    if sum_m >= 5000:
        sum_m -= 500
    return w * 10 / sum_m


def solution():
    w, m = map(int, stdin.readline().rstrip().split())
    curMax: float = getAnswer(m, w)
    answer: str = 'S'

    for i in range(2):
        w, m = map(int, stdin.readline().rstrip().split())
        cur: float = getAnswer(m, w)
        if cur > curMax:
            curMax = cur
            answer = 'N' if i == 0 else 'U'

    stdout.write("%s\n" % answer)


if __name__ == "__main__":
    solution()
