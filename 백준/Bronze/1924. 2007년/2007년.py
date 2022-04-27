from sys import stdin, stdout
import datetime


def solve():
  days: list = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
  x, y = map(int, stdin.readline().rstrip().split())
  stdout.write(str(days[datetime.datetime(2007, x, y).weekday()]))


if __name__ == "__main__":
    solve()
