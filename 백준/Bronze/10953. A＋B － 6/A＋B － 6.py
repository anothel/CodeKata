from sys import stdin, stdout


def solution():
    for _ in range(int(stdin.readline().rstrip())):
        s: list = list(map(int, stdin.readline().rstrip().split(",")))
        stdout.write("%d\n" % sum(s))


if __name__ == "__main__":
    solution()
