from sys import stdin, stdout


def solve():
    for _ in range(int(stdin.readline().rstrip())):
        num, j, k, s = map(int, stdin.readline().rstrip().split())
        sum: int = j + k + s
        stdout.write("%d %d " % (num, sum))
        if sum >= 55 and j >= 35 * 0.3 and k >= 25 * 0.3 and s >= 40 * 0.3:
            stdout.write("PASS\n")
        else:
            stdout.write("FAIL\n")


if __name__ == "__main__":
    solve()
