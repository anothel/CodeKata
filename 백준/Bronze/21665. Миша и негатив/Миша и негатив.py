from sys import stdin, stdout


def solution():
    n, m = map(int, stdin.readline().rstrip().split())
    table: list = list()
    for _ in range(n):
        table.append(list(map(str, stdin.readline().rstrip().split())))
    answer: int = 0

    _ = list(map(str, stdin.readline().rstrip().split()))
    for i in range(n):
        tmp: list = list(map(str, stdin.readline().rstrip().split()))
        for j in range(m):
            if table[i][0][j] == tmp[0][j]:
                answer += 1

    stdout.write("%d\n" % answer)


if __name__ == "__main__":
    solution()
