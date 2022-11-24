from sys import stdin, stdout


def solution():
    table: list = [0, 1, 1]

    n: int = int(stdin.readline().rstrip())
    
    for i in range(3, n+1):
        num: int = table[i - 1] + table[i - 2]
        table.append(num)


    stdout.write("%d\n" % table[n])


if __name__ == "__main__":
    solution()
