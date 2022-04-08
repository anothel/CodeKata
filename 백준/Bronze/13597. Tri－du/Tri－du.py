from sys import stdin, stdout


def main():
  stdout.write(str(max(map(int, stdin.readline().rstrip().split()))))


if __name__ == "__main__":
    main()
