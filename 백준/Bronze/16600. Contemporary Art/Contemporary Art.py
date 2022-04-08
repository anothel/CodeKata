from sys import stdin, stdout


def main():
  stdout.write(str("%.8f" % (int(stdin.readline().rstrip()) ** 0.5 * 4)))


if __name__ == "__main__":
  main()
