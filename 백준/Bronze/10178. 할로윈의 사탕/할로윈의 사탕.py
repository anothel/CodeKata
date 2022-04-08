from sys import stdin, stdout


def main():
  for _ in range(int(stdin.readline())):
    c, v = map(int, stdin.readline().rstrip().split())
    stdout.write(
        str("You get %d piece(s) and your dad gets %d piece(s).\n") % (c//v, c % v))


if __name__ == "__main__":
  main()
