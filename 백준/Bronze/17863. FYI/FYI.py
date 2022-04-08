from sys import stdin, stdout


def main():
  sList = list(stdin.readline().rstrip())

  stdout.write(
      str("YES" if sList[0] == "5" and sList[1] == "5" and sList[2] == "5" else "NO"))


if __name__ == "__main__":
  main()
