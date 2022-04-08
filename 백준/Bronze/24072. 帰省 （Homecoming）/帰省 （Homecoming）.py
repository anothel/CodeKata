from sys import stdin, stdout


def main():
  a, b, c = map(int, stdin.readline().rstrip().split())

  stdout.write(str(1 if a <= c and c < b else 0))


if __name__ == "__main__":
  main()
