from sys import stdin, stdout
import datetime


def solve():
    for _ in range(int(stdin.readline().rstrip())):
        y, m = map(int, stdin.readline().rstrip().split())
        dt = datetime.datetime(y, m, m)
        diff_datys = datetime.timedelta(days=m)
        answer = dt - diff_datys
        stdout.write("%d %d %d\n" % (answer.year, answer.month, answer.day))


if __name__ == "__main__":
    solve()
