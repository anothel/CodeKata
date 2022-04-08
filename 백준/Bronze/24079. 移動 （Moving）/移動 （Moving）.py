from sys import stdin, stdout


def main():
  x = int(stdin.readline().rstrip())
  y = int(stdin.readline().rstrip())
  z = int(stdin.readline().rstrip())

  stdout.write(str(1 if x+y <= z else 0))


if __name__ == "__main__":
  main()
