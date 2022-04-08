from sys import stdin, stdout


def main():
  pi = 3.14159265359
  stdout.write(str(2 * pi * (((int(stdin.readline().strip())) / pi) ** 0.5)))


if __name__ == "__main__":
    main()
