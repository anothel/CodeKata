from sys import stdin, stdout


def main():
  a1 = int(stdin.readline().rstrip())
  a2 = int(stdin.readline().rstrip())
  a3 = int(stdin.readline().rstrip())

  stdout.write(str(min(a2 * 2 + a3*4, a1*2+a3*2, a1*4+a2*2)))


if __name__ == "__main__":
    main()
