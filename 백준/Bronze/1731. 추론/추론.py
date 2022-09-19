from sys import stdin, stdout


def solution():
    nums: list = list()
    for i in range(int(stdin.readline().rstrip())):
        nums.append(int(stdin.readline().rstrip()))
    if nums[-1] - nums[-2] == nums[-2] - nums[-3]:
        stdout.write("%d\n" % (nums[-1] + nums[-2] - nums[-3]))
    else:
        stdout.write("%d\n" % (nums[-1] * (nums[-2] // nums[-3])))


if __name__ == "__main__":
    solution()
