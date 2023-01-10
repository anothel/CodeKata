from sys import stdin, stdout


def solution():
    n: int = int(stdin.readline().rstrip())
    c: list = list(map(int, stdin.readline().rstrip().split()))

    sum: int = 0
    for i in c:
        if i <= n:
            sum += i
        else:
            sum += n

    stdout.write("%d\n" % sum)


if __name__ == "__main__":
    solution()
