from sys import stdin, stdout


def solution():
    table: list = [0 for i in range(11)]

    table[1] = 1
    table[2] = 2
    table[3] = 4

    for i in range(4, 11):
        table[i] = table[i - 1] + table[i - 2] + table[i - 3]

    for _ in range(int(stdin.readline().rstrip())):
        stdout.write("%d\n" % table[int(stdin.readline().rstrip())])


if __name__ == "__main__":
    solution()
