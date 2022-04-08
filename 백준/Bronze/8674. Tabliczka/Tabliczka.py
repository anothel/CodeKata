from sys import stdin, stdout


def main():
  a = list(map(int, stdin.readline().strip().split()))

  if (a[0] % 2 != 0 and a[1] % 2 != 0):
    print(min(a[0], a[1]))
  else:
    print(0)


if __name__ == "__main__":
  main()
