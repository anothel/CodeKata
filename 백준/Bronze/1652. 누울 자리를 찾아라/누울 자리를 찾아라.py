from sys import stdin, stdout


def solution():
    table: list = list()
    n: int = int(stdin.readline().rstrip())
    for _ in range(n):
        table.append(list(stdin.readline().rstrip()))

    rawCount: int = 0
    for i in range(n):
        bed: bool = False
        next: bool = True
        for j in range(n):
            if bed == True and table[i][j] == '.' and next:
                rawCount += 1
                next = False
                
            elif bed == False and table[i][j] == '.':
                bed = True
            elif table[i][j] == 'X':
                bed = False
                next = True

    ColCount: int = 0
    for i in range(n):
        bed: bool = False
        next: bool = True
        for j in range(n):
            if bed == True and table[j][i] == '.' and next:
                ColCount += 1
                next = False
                
            elif bed == False and table[j][i] == '.':
                bed = True
            elif table[j][i] == 'X':
                bed = False
                next = True

    stdout.write("%d %d\n" % (rawCount, ColCount))


if __name__ == "__main__":
    solution()
