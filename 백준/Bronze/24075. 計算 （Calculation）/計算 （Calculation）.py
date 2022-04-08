from sys import stdin, stdout


def main():
  a, b = map(int, stdin.readline().rstrip().split())

  stdout.write(str(max(a+b, a-b)) + "\n")
  stdout.write(str(min(a+b, a-b)))


if __name__ == "__main__":
  main()
