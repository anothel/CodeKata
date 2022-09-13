from sys import stdin, stdout


def solution():
    nums: list = [0 for _ in range(10)]

    cur: int = 1
    for _ in range(3):
        cur *= int(stdin.readline().rstrip())

    while cur > 0:
        nums[(cur % 10)] += 1
        cur //= 10

    for i in nums:
        stdout.write("%d\n" % i)


if __name__ == "__main__":
    solution()
