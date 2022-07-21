from sys import stdin, stdout


def solve():
    people: list = list(map(int, stdin.readline().rstrip().split()))
    x, y, r = map(int, stdin.readline().rstrip().split())

    try:
        stdout.write("%d\n" % (people.index(x) + 1))
    except ValueError:
        stdout.write("0\n")


if __name__ == "__main__":
    solve()
