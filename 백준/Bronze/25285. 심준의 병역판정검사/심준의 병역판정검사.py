from sys import stdin, stdout


def getBMI(h: int, w: int) -> float:
    return w / (h * 0.01)**2


def solution():
    for _ in range(int(stdin.readline().rstrip())):
        h, w = map(int, stdin.readline().rstrip().split())
        answer: int = 0
        if h < 140.1:
            answer = 6
        elif 140.1 <= h and h < 146:
            answer = 5
        elif 146 <= h and h < 159:
            answer = 4
        elif 159 <= h and h < 161:
            bmi: float = getBMI(h, w)
            answer = 3 if 16 <= bmi and bmi < 35 else 4
        elif 161 <= h and h < 204:
            bmi: float = getBMI(h, w)
            if 20 <= bmi and bmi < 25:
                answer = 1
            elif (18.5 <= bmi and bmi < 20) or (25 <= bmi and bmi < 30):
                answer = 2
            elif (16 <= bmi and bmi < 18.5) or (30 <= bmi and bmi < 35):
                answer = 3
            elif 16 > bmi or 35 <= bmi:
                answer = 4
        else:
            answer = 4
        stdout.write("%d\n" % answer)


if __name__ == "__main__":
    solution()
