from sys import stdin, stdout


def solve():
    answer: int = 0
    a, b, c = map(int, stdin.readline().rstrip().split())
    n: int = int(stdin.readline().rstrip())
    for _ in range(n):
        curValue: int = 0
        for _ in range(3):
            atmp, btmp, ctmp = map(int, stdin.readline().rstrip().split())
            curValue += atmp * a
            curValue += btmp * b
            curValue += ctmp * c
        if curValue > answer:
            answer = curValue

    stdout.write("%d\n" % (answer))


if __name__ == "__main__":
    solve()
