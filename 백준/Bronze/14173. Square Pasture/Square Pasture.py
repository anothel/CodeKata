from sys import stdin, stdout


def main():
  x1, y1, x2, y2 = map(int, stdin.readline().rstrip().split())
  x1_, y1_, x2_, y2_ = map(int, stdin.readline().rstrip().split())

  a = max(x1, x2, x1_, x2_) - min(x1, x2, x1_, x2_)
  b = max(y1, y2, y1_, y2_) - min(y1, y2, y1_, y2_)

  stdout.write(str(a**2 if a > b else b**2))


if __name__ == "__main__":
    main()
