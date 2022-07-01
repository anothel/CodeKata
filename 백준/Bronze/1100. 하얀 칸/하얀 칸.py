from sys import stdin, stdout


def solution():
    answer: int = 0
    for i in range(1, 9):
        ches: list = list(stdin.readline().rstrip())
        if i % 2 != 0:
            for j in range(1, 9):
                if j % 2 != 0 and ches[j - 1] == "F":
                    answer += 1
        else:
            for j in range(1, 9):
                if j % 2 == 0 and ches[j - 1] == "F":
                    answer += 1
    stdout.write("%d\n" % answer)


if __name__ == "__main__":
    solution()
