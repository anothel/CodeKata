from sys import stdin, stdout


def main():
  stdout.write(str((int(stdin.readline().strip()) ** 0.5) * 4))


if __name__ == "__main__":
    main()
