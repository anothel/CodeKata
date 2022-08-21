from sys import stdin, stdout


def makeMin(nums: list):
    for i in range(len(nums)):
        if nums[i] == '6':
            nums[i] = '5'


def makeMax(nums: list):
    for i in range(len(nums)):
        if nums[i] == '5':
            nums[i] = '6'


def makeNumber(nums: list) -> int:
    tmp: str = ''
    for i in nums:
        tmp += i
    return int(tmp)


def solution():
    ansMin: int = 0
    ansMax: int = 0
    a, b = map(str, stdin.readline().rstrip().split())
    listA: list = list(a)
    listB: list = list(b)

    makeMin(listA)
    makeMin(listB)
    ansMin = makeNumber(listA) + makeNumber(listB)

    makeMax(listA)
    makeMax(listB)
    ansMax = makeNumber(listA) + makeNumber(listB)

    stdout.write("%d %d\n" % (ansMin, ansMax))


if __name__ == "__main__":
    solution()
