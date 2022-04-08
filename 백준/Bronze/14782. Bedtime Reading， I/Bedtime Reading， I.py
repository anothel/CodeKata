from sys import stdin, stdout


def main():
  I = int(stdin.readline().strip())

  sum: int = 0
  for i in range(1, I+1):
    if I % i == 0:
      sum += i

  stdout.write(str(sum))


if __name__ == "__main__":
    main()
