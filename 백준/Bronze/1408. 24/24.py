from sys import stdin, stdout
import datetime


def solution():
  hh1, mm1, ss1 = map(int, stdin.readline().rstrip().split(":"))
  hh2, mm2, ss2 = map(int, stdin.readline().rstrip().split(":"))

  if hh1 > hh2 or (hh1 <= hh2 and mm1 > mm2) or (hh1 <= hh2 and mm1 <= mm2 and ss1 > ss2):
    dt = datetime.datetime(2022, 4, 19, hh2, mm2, ss2) - \
        datetime.datetime(2022, 4, 18, hh1, mm1, ss1)
    stdout.write("%02d:%02d:%02d" %
                 (dt.seconds//3600, (dt.seconds % 3600) // 60, (dt.seconds % 60) % 60))
  else:
    dt = datetime.datetime(2022, 4, 18, hh2, mm2, ss2) - \
        datetime.datetime(2022, 4, 18, hh1, mm1, ss1)
    stdout.write("%02d:%02d:%02d" %
                 (dt.seconds//3600, (dt.seconds % 3600)//60, (dt.seconds % 60) % 60))


if __name__ == "__main__":
    solution()
