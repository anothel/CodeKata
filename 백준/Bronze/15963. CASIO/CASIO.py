from sys import stdin, stdout


def main():
  n, m = map(int, stdin.readline().rstrip().split())
  stdout.write(str(1 if m == n else 0))


if __name__ == "__main__":
  main()
