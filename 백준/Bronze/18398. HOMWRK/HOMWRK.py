from sys import stdin, stdout


def solution():
    for _ in range(int(stdin.readline().rstrip())):
        for _ in range(int(stdin.readline().rstrip())):
            a, b = map(int, stdin.readline().rstrip().split())
            stdout.write("%d %d\n" % (a + b, a * b))


if __name__ == "__main__":
    solution()
