from sys import stdin, stdout


def solve():
    for _ in range(int(stdin.readline().rstrip()) // 4):
        stdout.write("long ")
    stdout.write("int\n")


if __name__ == "__main__":
    solve()
