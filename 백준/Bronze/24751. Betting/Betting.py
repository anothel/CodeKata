from sys import stdin, stdout


def main():
  a = int(stdin.readline().rstrip())
  
  stdout.write(str(100/a) + "\n")
  stdout.write(str(100/(100-a)))


if __name__ == "__main__":
    main()
