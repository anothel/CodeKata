from sys import stdin, stdout


def solution():
    a, b = map(int, stdin.readline().rstrip().split())
    answer: int = a // 2
    stdout.write("%d\n" % answer if answer < b else "%d\n" % b)


if __name__ == "__main__":
    solution()