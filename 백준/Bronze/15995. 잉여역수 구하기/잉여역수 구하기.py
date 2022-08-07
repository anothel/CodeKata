from sys import stdin, stdout


def solution():
    a, m = map(int, stdin.readline().rstrip().split())
    i: int = 1
    while True:
        if (1 + (m * i)) % a == 0:
            break
        i += 1
    stdout.write("%d\n" % ((1 + (m * i)) / a))


if __name__ == "__main__":
    solution()
