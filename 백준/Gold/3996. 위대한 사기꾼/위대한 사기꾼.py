from sys import stdin, stdout


def main():
    n, k = map(int, stdin.readline().split())

    sReturn: list = list()

    while n:
        sReturn.insert(0, n % (k * k))
        n //= k * k

    count: int = 0
    f: int = 0

    for i in sReturn:
        if f == 0:
            if k <= i:
                count += k
                f = 1
            else:
                count += i
        count *= k

    count //= k
    if (f == 0):
        count += 1

    stdout.write("%d\n" % count)


if __name__ == "__main__":
    main()
