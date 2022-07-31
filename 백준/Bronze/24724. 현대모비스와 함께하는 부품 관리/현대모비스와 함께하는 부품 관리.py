from sys import stdin, stdout


def solve():
    for i in range(int(stdin.readline().rstrip())):
        stdout.write("Material Management %d\n" % (i + 1))
        for _ in range(int(stdin.readline().rstrip()) + 1):
            atmp, btmp = map(int, stdin.readline().rstrip().split())
        stdout.write("Classification ---- End!\n")


if __name__ == "__main__":
    solve()
