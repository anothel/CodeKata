from sys import stdin, stdout


def solution():
    while True:
        try:
            n, s = map(int, stdin.readline().rstrip().split())
            stdout.write("%d\n" % (s // (n + 1)))
        except:
            break


if __name__ == "__main__":
    solution()
