from sys import stdin, stdout


def main():

  stdout.write(str("%5f" % ((100 * 3.785411784) /
               (float(stdin.readline().rstrip()) * 1.609344))))


if __name__ == "__main__":
    main()
