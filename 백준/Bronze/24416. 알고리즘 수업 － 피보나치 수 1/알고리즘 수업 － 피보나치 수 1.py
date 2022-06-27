from sys import stdin, stdout


def fib(n: int, nums: list) -> int:
    if (n == 1 or n == 2):
        nums[0] += 1
        return 1  # 코드1
    else:
        return (fib(n - 1, nums) + fib(n - 2, nums))


def fibonacci(n: int, f: list, nums: list) -> int:
    f[1] = f[2] = 1
    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]  # 코드2
        nums[1] += 1
    return f[n]


def main():
    n: int = int(stdin.readline().rstrip())
    nums: list = [0, 0]
    # fib(n, nums)

    f: list = [0] * (n + 1)
    fibonacci(n, f, nums)

    stdout.write("%d %d\n" % (f[n], n - 2))


if __name__ == "__main__":
    main()