from itertools import count
from sys import stdin, stdout


def main():
  credits = sorted(map(int, stdin.readline().rstrip().split()))
  if credits[0] + credits[1] == credits[2]:
    stdout.write("S")
  elif 2 <= credits.count(credits[0]) or credits.count(credits[1]) == 2:
    stdout.write("S")
  else:
    stdout.write("N")


if __name__ == "__main__":
  main()
