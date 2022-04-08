from sys import stdin, stdout


def main():
  n = int(stdin.readline().rstrip())
  stdout.write(str("YONSEI" if n == 0 else "Leading the Way to the Future"))


if __name__ == "__main__":
  main()
