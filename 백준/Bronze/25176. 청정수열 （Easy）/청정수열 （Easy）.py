from sys import stdin, stdout


# 1 1 2 2
def getBetweenScore(n: int, nums: list) -> int:
    bFirstFind: bool = False
    nScore: int = 0
    for i in nums:
        if i == n and bFirstFind == False:
            bFirstFind == True
            nScore += i
        elif bFirstFind == True:
            nScore += i
            if i == n:
                break
    return nScore


def testFunc(aList: list, bList: list, nInsert: int):
    if len(bList) == len(aList):
        return

    for i in aList:
        if nInsert != -1:
            bList.append(nInsert)
        testFunc(aList, bList, i)


def main():
    n = int(stdin.readline().rstrip())
    answer: int = 1
    for i in range(1, n + 1):
        answer *= i
    stdout.write("%d\n" % answer)

    # nums: list = list()
    # for i in range(1, n + 1):
    #     nums.append(i)
    #     nums.append(i)

    # testList: list = list()
    # testFunc(nums, testList, -1)


if __name__ == "__main__":
    main()