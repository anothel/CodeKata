from sys import stdin, stdout


def solution():
    n: int = int(stdin.readline().rstrip())
    for _ in range(n):
        a, b = map(str, stdin.readline().rstrip().split())
        answer: int = int("0b" + a, 2) + int("0b" + b, 2)
        stdout.write("%s\n" % (bin(answer)[2:]))


if __name__ == "__main__":
    solution()
