from sys import stdin, stdout


def main():
  n = int(stdin.readline().rstrip())

  total: int = 0
  for i in range(n+1):
    for j in range(i+1):
      total += i+j
  stdout.write(str(total))


if __name__ == "__main__":
  main()
