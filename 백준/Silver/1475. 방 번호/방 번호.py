from sys import stdin, stdout


def solution():
    table: list = [0] * 10
    n: list = list(stdin.readline().rstrip())
    answer: int = 0

    for i in n:
        if table[int(i) - 1] == 0:
            if int(i) == 6 and table[8] != 0:
                table[8] -= 1
                continue
            elif int(i) == 9 and table[5] != 0:
                table[5] -= 1
                continue
            answer += 1
            for j in range(len(table)):
                table[j] += 1
        table[int(i) - 1] -= 1

    stdout.write("%d\n" % answer)


if __name__ == "__main__":
    solution()
