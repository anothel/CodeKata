from sys import stdin, stdout


def main():
  sum: int = 0
  while True:
    input = int(stdin.readline().strip())
    if input == -1:
      break
    sum += input
  stdout.write(str(sum))


if __name__ == "__main__":
    main()
