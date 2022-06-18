from math import pi
from sys import stdin, stdout


def main():
  i: int = 1
  while True:
    d, r, t = map(float, stdin.readline().rstrip().split())
    if r == 0:
        break
    dis = d/63360 * pi * r
    mph = dis / t * 3600
    stdout.write("Trip #%d: %.2f %.2f\n" % (i, dis, mph))
    i += 1


if __name__ == "__main__":
  main()
