from sys import stdin, stdout


def solution():
    n: int = int(stdin.readline().rstrip())
    p: int = int(stdin.readline().rstrip())

    nums: list = list()
    if n >= 20:
        nums.append(p * 0.75)
    elif n >= 10:
        nums.append(p * 0.9)

    if n >= 15:
        if p - 2000 < 0:
            nums.append(0)
        else:
            nums.append(p - 2000)
    elif n >= 5:
        if p - 500 < 0:
            nums.append(0)
        else:
            nums.append(p - 500)

    nums.append(p)

    stdout.write("%d\n" % (min(nums)))


if __name__ == "__main__":
    solution()