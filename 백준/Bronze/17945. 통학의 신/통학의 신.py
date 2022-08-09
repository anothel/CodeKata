from sys import stdin, stdout


def solution():
    a, b = map(int, stdin.readline().rstrip().split())
    answer1: int = 0
    answer2: int = 0
    if ((2 * a)**2) == 4 * b:
        answer1 = -(2 * a) / 2
    else:
        answer1 = (-(2 * a) + (((2 * a)**2) - 4 * b)**0.5) / 2
        answer2 = (-(2 * a) - (((2 * a)**2) - 4 * b)**0.5) / 2

    if answer2 == 0:
        stdout.write("%d\n" % answer1)
    else:
        stdout.write("%d %d\n" %
                     (min(answer1, answer2), max(answer1, answer2)))


if __name__ == "__main__":
    solution()
