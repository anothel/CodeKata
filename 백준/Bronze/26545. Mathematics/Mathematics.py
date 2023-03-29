from sys import stdin, stdout


def solution():

    n: int = int(stdin.readline().strip())
    answer: int = 0
    for _ in range(n):
        answer += int(stdin.readline().strip())

    stdout.write("%d\n" % answer)


if __name__ == "__main__":
    solution()
