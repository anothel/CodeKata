from sys import stdin, stdout


def solve():
    while True:
        b, n = map(int, stdin.readline().rstrip().split())
        if b == 0 and n == 0:
            break
        answer: int = 0
        answerI: int = 0
        bIsFirst: bool = True
        for i in range(1, b + 1):
            tmp: int = abs(i**n - b)
            if bIsFirst == True:
                answer = tmp
                answerI = i
                bIsFirst = False
            elif tmp < answer:
                answer = tmp
                answerI = i
        stdout.write("%d\n" % answerI)


if __name__ == "__main__":
    solve()
