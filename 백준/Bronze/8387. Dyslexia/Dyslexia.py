from sys import stdin, stdout


def solution():
    _ = int(stdin.readline().rstrip())
    mine: list = list(stdin.readline().rstrip())
    cor: list = list(stdin.readline().rstrip())

    answer: int = 0

    for i in range(len(mine)):
        if mine[i] == cor[i]:
            answer += 1

    stdout.write("%d\n" % answer)


if __name__ == "__main__":
    solution()
