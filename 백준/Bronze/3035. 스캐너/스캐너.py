from sys import stdin, stdout


def solution():
    r, c, zr, zc = map(int, stdin.readline().rstrip().split())

    table: list = list()
    for _ in range(r):
        table.append(list(stdin.readline().rstrip()))

    for j in range(len(table)):
        tmp: str = ''
        for k in range(len(table[j])):
            for _ in range(zc):
                tmp += table[j][k]
        table[j] = list(tmp)

    for i in range(len(table)):
        for _ in range(zr):
            stdout.write("%s\n" % ''.join(table[i]))


if __name__ == "__main__":
    solution()