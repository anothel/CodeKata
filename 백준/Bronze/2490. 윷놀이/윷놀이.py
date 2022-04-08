from sys import stdin, stdout


def main():
  for _ in range(3):
    a, b, c, d = map(int, stdin.readline().strip().split())
    sReturn: str = ""

    if a+b+c+d == 1:
      sReturn = "C"
    elif a+b+c+d == 2:
      sReturn = "B"
    elif a+b+c+d == 3:
      sReturn = "A"
    elif a+b+c+d == 0:
      sReturn = "D"
    elif a+b+c+d == 4:
      sReturn = "E"

    stdout.write(sReturn + "\n")


if __name__ == "__main__":
    main()
