from sys import stdin, stdout


def main():
  n = int(stdin.readline().strip())
  
  if n % 2 != 0:
    stdout.write(str(0))
  else:
    if n % 4 == 0:
      stdout.write(str(2))
    else:
      stdout.write(str(1))




if __name__ == "__main__":
    main()
