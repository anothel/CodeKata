from sys import stdin, stdout


def solution():
    _: int = int(stdin.readline().rstrip())
    numsA: list = sorted(map(int, stdin.readline().rstrip().split()))
    numsA.reverse()
    numsB: list = sorted(map(int, stdin.readline().rstrip().split()))

    answer: int = 0

    for i in range(len(numsA)):
        answer += numsA[i] * numsB[i]

    stdout.write("%d\n" % answer)


if __name__ == "__main__":
    solution()
