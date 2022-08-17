from sys import stdin, stdout


def solution():
    n, k = map(int, stdin.readline().rstrip().split())
    nums: list = sorted(map(int, stdin.readline().rstrip().split()))
    stdout.write("%d\n" % nums[-k])


if __name__ == "__main__":
    solution()
