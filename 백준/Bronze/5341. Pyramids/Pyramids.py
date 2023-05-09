from sys import stdin


def CalcBlock(n: int) -> int:
    result: int = 0
    for i in range(1, n + 1):
        result += i
    return result


def solution():
    while True:
        num: int = int(stdin.readline().rstrip())
        if num == 0:
            break
        print(CalcBlock(num))


if __name__ == "__main__":
    solution()
