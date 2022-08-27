from sys import stdin, stdout


def solution():
    _ = int(stdin.readline().rstrip())
    nums: list = list(map(int, stdin.readline().rstrip().split()))
    myNums: list = [0]

    answer: int = 0

    for i in nums:
        if i == myNums[-1] + 1:
            myNums.append(i)
            continue
        else:
            answer += 1

    stdout.write("%d\n" % answer)


if __name__ == "__main__":
    solution()
