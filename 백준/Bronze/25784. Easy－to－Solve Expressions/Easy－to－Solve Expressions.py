from sys import stdin, stdout


def solution():
    a, b, c = map(int, stdin.readline().rstrip().split())

    if a + b == c or a + c == b or b + c == a:
        stdout.write("%d\n" % 1)
    elif a * b == c or a * c == b or b * c == a:
        stdout.write("%d\n" % 2)
    else:
        stdout.write("%d\n" % 3)


if __name__ == "__main__":
    solution()
