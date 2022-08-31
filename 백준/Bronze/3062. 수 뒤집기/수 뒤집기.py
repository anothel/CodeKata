from sys import stdin, stdout


def isFalindrom(sen: str) -> bool:
    left: int = 0
    right: int = len(sen) - 1

    while left < right:
        if sen[left] == sen[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


def solution():
    for _ in range(int(stdin.readline().rstrip())):
        n: str = stdin.readline().rstrip()
        tmpList: list = list(n)
        tmpList.reverse()

        n_: str = ""
        for i in tmpList:
            n_ += i
        stdout.write("YES\n" if isFalindrom(str(int(n) +
                                                int(n_))) == True else "NO\n")


if __name__ == "__main__":
    solution()
