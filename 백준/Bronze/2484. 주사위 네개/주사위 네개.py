from sys import stdin, stdout


def solution():
    answers: list = list()
    for _ in range(int(stdin.readline().rstrip())):
        nums: list = sorted(map(int, stdin.readline().rstrip().split()))
        if len(set(nums)) == 1:
            answers.append(50000 + nums[0] * 5000)
        elif len(set(nums)) == 2:
            if nums[1] == nums[2]:
                answers.append(10000 + nums[1] * 1000)
            else:
                answers.append(2000 + nums[0] * 500 + nums[2] * 500)
        else:
            for i in range(3):
                if nums[i] == nums[i + 1]:
                    answers.append(1000 + nums[i] * 100)
                    continue
            answers.append(nums[3] * 100)

    stdout.write("%d\n" % max(answers))


if __name__ == "__main__":
    solution()