from sys import stdin, stdout


def main():
  x, y = map(int, stdin.readline().rstrip().split())
  r: int = int(stdin.readline().rstrip())

  stdout.write(str(x-r) + " " + str(y + r) + " \n")
  stdout.write(str(x+r) + " " + str(y + r) + " \n")
  stdout.write(str(x+r) + " " + str(y - r) + " \n")
  stdout.write(str(x-r) + " " + str(y - r) + " \n")


if __name__ == "__main__":
  main()
