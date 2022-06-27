from sys import stdin, stdout


def solve():
    r = int(stdin.readline().rstrip())
    c = int(stdin.readline().rstrip())
    for _ in range(r):
        for _ in range(c):
            stdout.write("*")
        stdout.write("\n")


if __name__ == "__main__":
    solve()
