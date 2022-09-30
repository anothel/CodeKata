from sys import stdin, stdout


def solution():
    mine: str = stdin.readline().rstrip()
    nums: list = list()
    for _ in range(int(stdin.readline().rstrip())):
        nums.append(stdin.readline().rstrip())
    stdout.write("%d\n" % nums.count(mine))


if __name__ == "__main__":
    solution()