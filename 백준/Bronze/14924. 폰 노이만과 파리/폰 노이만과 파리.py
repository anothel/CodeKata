from sys import stdin, stdout


def main():

  s, t, d = map(int, stdin.readline().rstrip().split())

  stdout.write(str((d//(2*s)) *t))


if __name__ == "__main__":
    main()
