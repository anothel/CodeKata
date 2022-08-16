from sys import stdin, stdout


def getNumber(s: int, e: int, num: list) -> int:
    answer: int = 1
    for i in range(s, e + 1):
        answer *= int(num[i])
    return answer


def checkYujin(num: str) -> bool:
    yujin: bool = False
    for i in range(0, len(list(num))):
        if getNumber(0, i, list(num)) == getNumber(i + 1,
                                                   len(list(num)) - 1,
                                                   list(num)):
            yujin = True
            break

    return yujin


def solution():
    num: str = stdin.readline().rstrip()
    if int(num) < 10:
        stdout.write("NO\n")
    else:
        stdout.write("YES\n" if checkYujin(num) else "NO\n")


if __name__ == "__main__":
    solution()
