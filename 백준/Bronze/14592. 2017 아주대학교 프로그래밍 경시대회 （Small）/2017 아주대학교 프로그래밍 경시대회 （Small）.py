from sys import stdin, stdout


def solve():
    nScore: int = 0
    nCount: int = 0
    nTime: int = 0
    answer: int = 0
    for i in range(int(stdin.readline().rstrip())):
        a, b, c = map(int, stdin.readline().rstrip().split())
        if i == 0:
            nScore = a
            nCount = b
            nTime = c
            answer = i + 1
            continue

        if a > nScore:
            nScore = a
            answer = i + 1
            continue
        elif a < nScore:
            continue
        else:
            if b < nCount:
                nCount = b
                answer = i + 1
                continue
            elif b > nCount:
                continue
            else:
                if c < nTime:
                    c = nTime
                    answer = i + 1
                    continue
                else:
                    continue
    stdout.write("%d\n" % answer)


if __name__ == "__main__":
    solve()
