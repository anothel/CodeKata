from sys import stdin, stdout


def solution():
    a, b = map(str, stdin.readline().rstrip().split())

    c: str = int(a, 2) + int(b, 2)

    stdout.write("%s\n" % bin(c)[2:])


if __name__ == "__main__":
    solution()