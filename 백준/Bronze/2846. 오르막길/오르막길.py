from sys import stdin, stdout


def solution():
    _ = int(stdin.readline().rstrip())
    nums: list = list(map(int, stdin.readline().rstrip().split()))

    answer: int = 0
    tmpNums: list = list()
    for i in nums:
        if len(tmpNums) == 0:
            tmpNums.append(i)
            continue
        if i > tmpNums[-1]:
            tmpNums.append(i)
        else:
            tmp: int = max(tmpNums) - min(tmpNums)
            if tmp > answer:
                answer = tmp
            tmpNums.clear()
            tmpNums.append(i)
    tmp: int = max(tmpNums) - min(tmpNums)
    if tmp > answer:
        answer = tmp
    stdout.write("%d\n" % answer)


if __name__ == "__main__":
    solution()
