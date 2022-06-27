from sys import stdin, stdout


def fibonacci(n: int, f: list) -> int:
    f[1] = f[2] = 1
    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]  # 코드2
    return f[n]


def main():
    n: int = int(stdin.readline().rstrip())

    f: list = [0] * (n + 1)
    fibonacci(n, f)

    stdout.write("%d %d\n" % (f[n], n - 2))


if __name__ == "__main__":
    main()