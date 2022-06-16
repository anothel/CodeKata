from sys import stdin, stdout


def main():
  n, m = map(int, stdin.readline().rstrip().split())
  for _ in range(n):
    s: str = stdin.readline().rstrip()
    tmpList: list = list(s)
    tmpList.reverse()
    for i in tmpList:
      stdout.write("%s" % i)
    stdout.write("\n")


if __name__ == "__main__":
    main()
