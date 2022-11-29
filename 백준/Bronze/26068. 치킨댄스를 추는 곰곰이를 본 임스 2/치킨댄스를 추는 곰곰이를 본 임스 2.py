from sys import stdin, stdout


def solution():
    n: int = int(stdin.readline().rstrip())
    answer: int = 0
    for _ in range(n):
        s: str = stdin.readline().rstrip()[2:]
        if int(s) <= 90:
            answer += 1
    stdout.write("%d\n" % answer)


if __name__ == "__main__":
    solution()
