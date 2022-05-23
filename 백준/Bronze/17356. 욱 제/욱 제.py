from sys import stdin, stdout


def solve():
    a, b = map(int, stdin.readline().strip().split())
    m:float = (b-a)/400
    stdout.write("%.4f\n" % (1/(1+10**m)))


if __name__ == "__main__":
    solve()
