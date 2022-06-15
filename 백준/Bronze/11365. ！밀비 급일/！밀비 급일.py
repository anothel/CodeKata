from sys import stdin, stdout


def main():
  while True:
    pan: str = str(stdin.readline().rstrip())
    if pan == "END":
      break
    tmpList: list = list(pan)
    tmpList.reverse()
    for i in tmpList:
      stdout.write("%s" % i)
    stdout.write("\n")


if __name__ == "__main__":
    main()
