from sys import stdin, stdout


def solution():
    for _ in range(int(stdin.readline().rstrip())):
        nums: list = sorted(map(int, stdin.readline().rstrip().split()))
        stdout.write("%d\n" % nums[-3])


if __name__ == "__main__":
    solution()