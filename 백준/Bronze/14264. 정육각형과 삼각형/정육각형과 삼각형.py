from sys import stdin, stdout


def main():

  stdout.write(
      str("%.15f" %   float((int(stdin.readline().rstrip()) ** 2) * 3 ** 0.5 / 4)))


if __name__ == "__main__":
    main()
