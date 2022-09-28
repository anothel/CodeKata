from sys import stdin, stdout


def solution():
    for i in range(int(stdin.readline().rstrip())):
        nums: list = list(map(int, stdin.readline().rstrip().split()))
        tmp: list = sorted(nums[1:])
        tmp.reverse()

        answer: int = 0
        for j in range(len(tmp) - 1):
            if answer < tmp[j] - tmp[j + 1]:
                answer = tmp[j] - tmp[j + 1]

        stdout.write("Class %d\n" % (i + 1))
        stdout.write("Max %d, Min %d, Largest gap %d\n" %
                     (max(tmp), min(tmp), answer))


if __name__ == "__main__":
    solution()