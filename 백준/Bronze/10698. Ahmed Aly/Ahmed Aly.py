from sys import stdin, stdout


def getAnswer(a: int, b: int, op: str, result: int) -> bool:
    return True if (op == "+" and a + b == result) or (op == "-" and a -
                                                       b == result) else False


def solve():
    for i in range(int(stdin.readline().rstrip())):
        nums: list = list(map(str, stdin.readline().rstrip().split()))
        stdout.write("Case %d: YES\n" %
                     (i + 1) if getAnswer(int(nums[0]), int(nums[2]), nums[1],
                                          int(nums[4])) else "Case %d: NO\n" %
                     (i + 1))


if __name__ == "__main__":
    solve()
