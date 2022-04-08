from sys import stdin, stdout


def main():
  a = sorted(map(int, stdin.readline().rstrip().split()))

  stdout.write(str(a[2]-a[1] + a[1]-a[0]))


if __name__ == "__main__":
    main()
