from sys import stdin, stdout


def solution():
    for i in range(int(stdin.readline().rstrip())):
        t: int = int(stdin.readline().rstrip())
        stdout.write("Case %d:\n" % (i + 1))
        for j in range(1, 7):
            for k in range(j, 7):
                if j + k == t:
                    stdout.write("(%d,%d)\n" % (j, k))


if __name__ == "__main__":
    solution()
