from sys import stdin, stdout


def main():

  stdout.write(str(bin(int(stdin.readline(), 2)*int(stdin.readline(), 2))[2:]))


if __name__ == "__main__":
    main()
