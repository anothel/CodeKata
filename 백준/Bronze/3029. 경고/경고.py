from sys import stdin, stdout
import datetime


def solve():
  hh1, mm1, ss1 = map(int, stdin.readline().rstrip().split(":"))
  hh2, mm2, ss2 = map(int, stdin.readline().rstrip().split(":"))

  if hh2 == hh1 and mm2 == mm1 and ss2 == ss1:
    stdout.write(str("24:00:00" + "\n"))
    return

  dt: datetime = datetime.datetime(
      2022, 4, 12 if hh2 < hh1 or (hh2 == hh1 and mm2 < mm1) or (hh2 == hh1 and mm2 == mm1 and ss2 < ss1) else 11, hh2, mm2, ss2) - datetime.datetime(2022, 4, 11, hh1, mm1, ss1)

  stdout.write(str("%02d:%02d:%02d" % (dt.seconds // 3600,
               (dt.seconds % 3600) // 60, dt.seconds % 60)) + "\n")


def main():
  solve()


if __name__ == "__main__":
    main()
