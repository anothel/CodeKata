from sys import stdin, stdout


def solution():
    nums: dict = {}
    sumValue: int = 0
    for i in range(8):
        nums[i + 1] = int(stdin.readline().rstrip())
    sortedNums: dict = sorted(nums.items(), key=lambda item: item[1])
    answer: list = list()

    for i in range(3, 8):
        answer.append(sortedNums[i][0])
        sumValue += sortedNums[i][1]

    stdout.write("%d\n" % sumValue)
    answer.sort()
    for i in answer:
        stdout.write("%d " % i)


if __name__ == "__main__":
    solution()
