from sys import stdin, stdout


def main():
  a: list = sorted(map(int, stdin.readline().rstrip().split()))

  stdout.write(str(a[2] - a[0] + a[2] - a[1]))


if __name__ == "__main__":
  main()
