from sys import stdin, stdout


def main():
  x, y = map(int, stdin.readline().rstrip().split())
  price: int = 1000*x/y
  for _ in range(int(stdin.readline().rstrip())):
    a, b = map(int, stdin.readline().rstrip().split())
    if 1000*a/b < price:
      price = 1000*a/b

  stdout.write(str("%.2f" % price))


if __name__ == "__main__":
    main()
