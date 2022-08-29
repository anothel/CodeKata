from sys import stdin, stdout


def initLove(word: list, nums: list):
    nums.append(word.count("L"))
    nums.append(word.count("O"))
    nums.append(word.count("V"))
    nums.append(word.count("E"))


def setLove(word: list, nums: list):
    for i in word:
        if i == "L":
            nums[0] += 1
        elif i == "O":
            nums[1] += 1
        elif i == "V":
            nums[2] += 1
        elif i == "E":
            nums[3] += 1


def getWin(nums: list) -> int:
    return ((nums[0] + nums[1]) * (nums[0] + nums[2]) * (nums[0] + nums[3]) *
            (nums[1] + nums[2]) * (nums[1] + nums[3]) *
            (nums[2] + nums[3])) % 100


def solution():
    green: str = stdin.readline().rstrip()

    curWin: int = 0
    answer: str = ""

    nameTable: list = [0 for _ in range(4)]
    setLove(list(green), nameTable)

    for _ in range(int(stdin.readline().rstrip())):
        tmpNameTable: list = list(nameTable)
        curName: str = stdin.readline().rstrip()
        setLove(list(curName), tmpNameTable)
        tmpWin: int = getWin(tmpNameTable)
        if tmpWin > curWin:
            curWin = tmpWin
            answer = curName
        elif tmpWin == curWin:
            if answer == "" or curName < answer:
                answer = curName
    stdout.write("%s\n" % answer)


if __name__ == "__main__":
    solution()
