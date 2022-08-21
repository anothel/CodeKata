from sys import stdin, stdout


def solution():
    n: int = int(stdin.readline().rstrip())
    nums: list = list(map(int, stdin.readline().rstrip().split()))

    answers: list = list()
    for i in range(len(nums)):
        tmp: list = list(nums)
        tmp.remove(tmp[i])
        answers.append(sum(tmp))
    stdout.write("%d\n" % min(answers))


if __name__ == "__main__":
    solution()
