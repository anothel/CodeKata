from sys import stdin, stdout


def solution():
    n: int = int(stdin.readline().rstrip())
    for i in range(n):
        m: int = int(stdin.readline().rstrip())
        table: list = list()
        for j in range(m):
            tmpList: list() = list(map(int, stdin.readline().rstrip().split()))
            table.append(tmpList)
        k, d, a = map(int, stdin.readline().rstrip().split())

        answer: int = 0
        for l in table:
            tmp: int = l[0] * k - l[1] * d + l[2] * a
            if tmp < 0:
                tmp = 0
            answer += tmp

        stdout.write("%d\n" % answer)


if __name__ == "__main__":
    solution()