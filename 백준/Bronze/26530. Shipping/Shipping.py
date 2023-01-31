from sys import stdin, stdout


def solution():
    n: int = int(stdin.readline().rstrip())
    for _ in range(n):
        x: int = int(stdin.readline().rstrip())
        total: int = 0
        for _ in range(x):
            _, each, price = map(str, stdin.readline().split())
            total += int(each) * float(price)
        stdout.write("$%.2f\n" % total)


if __name__ == "__main__":
    solution()
