from sys import stdin, stdout


def calc(a: int, b: int, s: str) -> int:
    answer: int = 0
    if s == "+":
        answer = a + b
    elif s == "-":
        answer = a - b
    elif s == "*":
        answer = a * b
    elif s == "/":
        if a < 0:
            a *= -1
            answer = a // b
            answer *= -1
        elif b < 0:
            b *= -1
            answer = a // b
            answer *= -1
        else:
            answer = a // b

    return answer


def solve():
    nums: list = list(map(str, stdin.readline().rstrip().split()))
    vs: list = list()
    vs.append(
        calc(calc(int(nums[0]), int(nums[2]), nums[1]), int(nums[4]), nums[3]))
    vs.append(
        calc(int(nums[0]), calc(int(nums[2]), int(nums[4]), nums[3]), nums[1]))

    stdout.write("%d\n" % min(vs))
    stdout.write("%d\n" % max(vs))


if __name__ == "__main__":
    solve()
