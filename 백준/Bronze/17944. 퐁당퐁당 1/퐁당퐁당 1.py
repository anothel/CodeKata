from sys import stdin, stdout


def solution():
    n, t = map(int, stdin.readline().rstrip().split())
    curHands: int = 0
    curIndex: int = 0
    isUp: bool = True
    while True:
        curIndex += 1
        if isUp == True:
            curHands += 1
        else:
            curHands -= 1

        if curHands == 2 * n and isUp == True:
            isUp = False
        elif isUp == False and curHands == 1:
            isUp = True
        if curIndex == t:
            break
    stdout.write("%d\n" % curHands)


if __name__ == "__main__":
    solution()
