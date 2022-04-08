from sys import stdin, stdout


def main():
  stdout.write(str(sorted(map(int, stdin.readline().rstrip().split()))[1]))


if __name__ == "__main__":
  main()
