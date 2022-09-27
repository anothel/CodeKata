from sys import stdin, stdout


def solution():
    sentense: list = list(stdin.readline().rstrip())

    ioi_c: int = 0
    joi_c: int = 0

    for i in range(len(sentense) - 2):
        if sentense[i:i + 3] == list("IOI"):
            ioi_c += 1
        if sentense[i:i + 3] == list("JOI"):
            joi_c += 1

    stdout.write("%d\n" % joi_c)
    stdout.write("%d\n" % ioi_c)


if __name__ == "__main__":
    solution()