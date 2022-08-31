from sys import stdin, stdout


def solution():
    n: int = int(stdin.readline().rstrip())

    table: list = [0 for i in range(n + 1)]

    for i in range(2, n + 1):
        table[i] = table[i - 1] + 1
        if i % 2 == 0:
            table[i] = min(table[i], table[i // 2] + 1)
        if i % 3 == 0:
            table[i] = min(table[i], table[i // 3] + 1)

    stdout.write("%d\n" % table[n])


if __name__ == "__main__":
    solution()
