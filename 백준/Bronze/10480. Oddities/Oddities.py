from sys import stdin, stdout


def solution():
    n: int = int(stdin.readline().rstrip())
    for _ in range(n):
        a: int = int(stdin.readline().rstrip())
        if a % 2 == 0:
            stdout.write("%d is even\n" % a)
        else:
            stdout.write("%d is odd\n" % a)


if __name__ == "__main__":
    solution()
