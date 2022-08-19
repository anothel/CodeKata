from sys import stdin, stdout


def solution():
    goldCount: int = 0
    goldTeam: bool = True
    for _ in range(int(stdin.readline().rstrip())):
        stars: int = 0
        plus: int = int(stdin.readline().rstrip())
        stars += plus * 5
        minus: int = int(stdin.readline().rstrip())
        stars -= minus * 3
        if stars <= 40:
            goldTeam = False
        else:
            goldCount += 1
    stdout.write("%d" % goldCount)
    stdout.write("+\n" if goldTeam == True else "\n")


if __name__ == "__main__":
    solution()
