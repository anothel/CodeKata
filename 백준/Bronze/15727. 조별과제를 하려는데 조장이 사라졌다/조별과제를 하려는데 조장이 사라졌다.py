from sys import stdin, stdout


def main():
  N = int(stdin.readline().strip())
  for i in range(N+1):
    if N <= 5 * i:
      break
  print(i)


if __name__ == "__main__":
    main()
