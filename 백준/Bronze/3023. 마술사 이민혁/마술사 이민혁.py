from sys import stdin, stdout


def work_width(table: list):
    tmp: list = list(table)
    tmp.reverse()
    for i in tmp:
        table.append(i)


def solution():
    r, c = map(int, stdin.readline().rstrip().split())
    table: list = list()
    for _ in range(r):
        table.append(list(stdin.readline().rstrip()))
    a, b = map(int, stdin.readline().rstrip().split())

    for i in table:
        work_width(i)

    for i in range(len(table) - 1, -1, -1):
        table.append(list(table[i]))

    table[a - 1][b - 1] = '.' if table[a - 1][b - 1] == '#' else '#'

    for i in table:
        for j in i:
            stdout.write("%s" % j)
        stdout.write("\n")


if __name__ == "__main__":
    solution()
