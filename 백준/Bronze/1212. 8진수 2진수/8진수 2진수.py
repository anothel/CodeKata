from sys import stdin, stdout


def main():

  stdout.write(str(bin(int(stdin.readline().rstrip(), 8))[2:]))


if __name__ == "__main__":
  main()
