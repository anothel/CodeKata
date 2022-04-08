from sys import stdin, stdout
import datetime


def main():
  # # n = int(stdin.readline().strip())
  # N, M = map(int, stdin.readline().strip().split())
  d, h, m = map(int, stdin.readline().strip().split())
  
  dt1 = datetime.datetime(2016, 11, 11, 11, 11)
  dt2 = datetime.datetime(2016, 11, d, h, m)
  ts = (dt2 - dt1).total_seconds()
  if ts < 0:
    print(-1)
  else:
    print(int(ts//60))
  
  # N = list(map(int, stdin.readline().strip().split()))
  # print(min(N)//2)
    
  # N.sort()
  # for i in N:
  #   stdout.write(str(i) + " ")

  # if M == 1 or M == 2:
  #   stdout.write(str("NEWBIE!"))
  # elif M <= N:
  #   stdout.write(str("OLDBIE!"))
  # else:
  #   stdout.write(str("TLE!"))
  # print(abs(N-M))


if __name__ == "__main__":
  main()
