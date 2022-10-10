from sys import stdin, stdout


def swap(a: int, b: int, l: list):
    tmp: int = l[a]
    l[a] = l[b]
    l[b] = tmp


def printL(l: list):
    for i in l:
        stdout.write("%d " % i)
    stdout.write("\n")


def check(l: list) -> bool:
    for i in range(5):
        if l[i] == i + 1:
            continue
        return False
    return True


def solution():
    nums: list = list(map(int, stdin.readline().rstrip().split()))
    while check(nums) == False:
        for i in range(4):
            if nums[i] > nums[i + 1]:
                swap(i, i + 1, nums)
                printL(nums)


if __name__ == "__main__":
    solution()