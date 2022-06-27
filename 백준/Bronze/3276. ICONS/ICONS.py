from sys import stdin, stdout


def solve():
    n = int(stdin.readline().rstrip())

    bIsFirst: bool = True
    answerI: int = 0
    answerJ: int = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i * j >= n:
                if bIsFirst == True:
                    answer = i + j
                    answerI = i
                    answerJ = j
                    bIsFirst = False
                elif i + j < answer:
                    answer = i + j
                    answerI = i
                    answerJ = j

    stdout.write("%d %d\n" % (answerI, answerJ))


if __name__ == "__main__":
    solve()
