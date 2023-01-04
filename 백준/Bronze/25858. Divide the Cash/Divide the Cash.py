from sys import stdin, stdout


def solution():
    n, d = map(int, stdin.readline().rstrip().split())

    problem: list = list()
    sum: int = 0

    for _ in range(n):
        i: int = int(stdin.readline().rstrip())
        problem.append(i)
        sum += i

    d //= sum
    for i in problem:
        stdout.write("%d\n" % (i * d))


if __name__ == "__main__":
    solution()
