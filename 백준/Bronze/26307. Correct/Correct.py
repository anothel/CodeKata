from sys import stdin, stdout


def solution():
    HH, MM = map(int, stdin.readline().rstrip().split())
    answer: int = 0

    answer += (HH - 9) * 60
    answer += MM
    stdout.write("%d" % answer)


if __name__ == "__main__":
    solution()
