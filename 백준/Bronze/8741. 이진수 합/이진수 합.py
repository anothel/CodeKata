from sys import stdin, stdout


def solution():
    k: int = int(stdin.readline().rstrip())
    t: int = 2**k - 1
    asnwer: int = t * (t + 1) // 2

    stdout.write("%s\n" % bin(asnwer)[2:])


if __name__ == "__main__":
    solution()