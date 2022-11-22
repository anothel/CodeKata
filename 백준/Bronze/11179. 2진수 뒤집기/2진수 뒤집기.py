from sys import stdin, stdout


def solution():
    n: int = int(stdin.readline().rstrip())
    b: list = list(bin(n)[2:])
    b.reverse()
    answer: int = int('0b' + ''.join(s for s in b), 2)

    stdout.write("%d\n" % answer)


if __name__ == "__main__":
    solution()
