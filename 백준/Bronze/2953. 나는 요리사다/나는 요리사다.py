from sys import stdin, stdout


def main():
  maxP: int = 0
  index: int = 0
  for i in range(5):
    a, b, c, d = map(int, stdin.readline().strip().split())
    tryMax: int = a+b+c+d
    if maxP < tryMax:
      maxP = tryMax
      index = i+1

  stdout.write(str(index) + "\n" + str(maxP))


if __name__ == "__main__":
    main()
