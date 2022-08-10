from sys import stdin, stdout


def changeDirect(n: int) -> int:
    return 1 if n == 0 else 0


def checkMonster(ari: list, sr: int, sc: int) -> bool:
    return True if ari[0] == sr and ari[1] == sc else False


def solution():
    n, m = map(int, stdin.readline().rstrip().split())
    a, d = map(int, stdin.readline().rstrip().split())
    sr, sc = map(int, stdin.readline().rstrip().split())

    curAri: list = [1, a]
    curDirect: int = d
    meetMonster: bool = False

    while not (curAri[0] == n and curAri[1] == m) and meetMonster == False:
        if curDirect == 0:
            while curAri[1] > 1 and meetMonster == False:
                curAri[1] -= 1
                if checkMonster(curAri, sr, sc) == True:
                    meetMonster = True
        else:
            while curAri[1] < m and meetMonster == False:
                curAri[1] += 1
                if checkMonster(curAri, sr, sc) == True:
                    meetMonster = True
        if meetMonster == True:
            break
        curAri[0] += 1
        if checkMonster(curAri, sr, sc) == True:
            meetMonster = True

        curDirect = changeDirect(curDirect)
    stdout.write("YES!\n" if meetMonster == False else "NO...\n")


if __name__ == "__main__":
    solution()
