from sys import stdin, stdout


def getJinSum(n: int) -> int:
    nRv: int = 1
    for i in range(2, n):
        if n % i == 0:
            nRv += i
    return nRv


def solve():
    nums: list = list(map(int, stdin.read().rstrip().split()))
    for i in nums:
        if i == 0:
            break
        elif i == 1:
            stdout.write("%d DEFICIENT\n" % i)
            continue

        if getJinSum(i) < i:
            stdout.write("%d DEFICIENT\n" % i)
        elif getJinSum(i) == i:
            stdout.write("%d PERFECT\n" % i)
        elif getJinSum(i) > i:
            stdout.write("%d ABUNDANT\n" % i)


if __name__ == "__main__":
    solve()
