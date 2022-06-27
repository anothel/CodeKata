from sys import stdin, stdout


def main():
    s: str = stdin.readline().rstrip()
    stdout.write("%s\n" % s.upper())


if __name__ == "__main__":
    main()
