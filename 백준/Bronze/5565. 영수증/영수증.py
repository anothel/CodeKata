from sys import stdin, stdout


def main():
  total: int = int(stdin.readline().rstrip())
  price: int = 0
  for i in range(9):
    price += int(stdin.readline().rstrip())

  stdout.write(str(total - price))


if __name__ == "__main__":
    main()
