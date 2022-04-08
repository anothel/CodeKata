from sys import stdin, stdout


def main():
  sList = list(map(int, stdin.readline().rstrip().split()))

  if 100 <= sum(sList):
    stdout.write(str("OK"))
  else:
    i: int = sList.index(min(sList))
    if i == 0:
      stdout.write(str("Soongsil"))
    elif i == 1:
      stdout.write(str("Korea"))
    elif i == 2:
      stdout.write(str("Hanyang"))


if __name__ == "__main__":
  main()
