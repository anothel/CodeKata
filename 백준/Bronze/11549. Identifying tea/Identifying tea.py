from itertools import count
from sys import stdin, stdout


def main():
  T: int = int(stdin.readline().rstrip())
  teaes: list = list(map(int, stdin.readline().rstrip().split()))

  stdout.write(str(teaes.count(T)))


if __name__ == "__main__":
  main()
