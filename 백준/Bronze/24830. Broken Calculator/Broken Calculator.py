from sys import stdin, stdout


def brokenCalculator(a: int, b: int, op: str, be: int) -> int:
    answer: int = 0

    if op == '+':
        answer = a + b - be
    elif op == '-':
        answer = (a - b) * be
    elif op == '*':
        answer = (a * b)**2
    elif op == '/':
        if a % 2 == 0:
            answer = a // 2
        else:
            answer = (a + 1) // 2

    return answer


if __name__ == "__main__":
    curNum: int = 1
    for _ in range(int(stdin.readline().rstrip())):
        nums: list = list(map(str, stdin.readline().rstrip().split()))
        curNum = brokenCalculator(int(nums[0]), int(nums[2]), nums[1], curNum)
        stdout.write("%d\n" % curNum)
