from sys import stdin, stdout


def solution():
    a, b = map(int, stdin.readline().rstrip().split())
    i: int = 0
    addCount: int = a - 2
    curNumber: int = 1
    curCount: int = 1
    while True:
        i += 1
        curNumber += addCount
        curCount += curNumber
        if i == b:
            break
    stdout.write("%d\n" % curCount)


if __name__ == "__main__":
    solution()
