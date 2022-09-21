from sys import stdin, stdout
import datetime


def solution():
    days = {
        '-': 0,
        '\\': 1,
        '(': 2,
        '@': 3,
        '?': 4,
        '>': 5,
        '&': 6,
        '%': 7,
        '/': -1
    }

    try:
        while True:
            num8: list = list(stdin.readline().rstrip())
            answer: int = 0
            for i in range(len(num8)):
                answer += days[num8[i]] * 8**(len(num8) - 1 - i)
            stdout.write("%d\n" % answer)
    except:
        return


if __name__ == "__main__":
    solution()
