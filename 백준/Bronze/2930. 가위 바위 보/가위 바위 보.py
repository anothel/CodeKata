from sys import stdin, stdout


def getMyScore(mine: str, yours: str) -> int:
    score: int = 0
    if mine == 'R' and yours == 'S':
        score = 2
    elif mine == 'R' and yours == 'R':
        score = 1
    elif mine == 'S' and yours == 'P':
        score = 2
    elif mine == 'S' and yours == 'S':
        score = 1
    elif mine == 'P' and yours == 'R':
        score = 2
    elif mine == 'P' and yours == 'P':
        score = 1
    return score


def getExpectScore(r: int, frds: list) -> int:
    answer: int = 0

    for i in range(r):
        nums: list = [0 for _ in range(3)]
        for frd in frds:
            nums[0] += getMyScore('R', frd[i])
            nums[1] += getMyScore('S', frd[i])
            nums[2] += getMyScore('P', frd[i])
        answer += max(nums)

    return answer


def solution():
    r: int = int(stdin.readline().rstrip())
    sng: list = list(stdin.readline().rstrip())
    n: int = int(stdin.readline().rstrip())
    frds: list = list()
    curScore: int = 0

    for _ in range(n):
        frd: list = list(stdin.readline().rstrip())
        frds.append(frd)
        for i in range(len(frd)):
            curScore += getMyScore(sng[i], frd[i])

    stdout.write("%d\n%d\n" % (curScore, getExpectScore(r, frds)))


if __name__ == "__main__":
    solution()
