from sys import stdin, stdout


def main():

  a, b, c = map(int, stdin.readline().rstrip().split())

  stdout.write(str(int(a*b/c) if a/b*c < a*b/c else int(a/b*c)))


if __name__ == "__main__":
    main()
