from sys import stdin, stdout


def main():
  for _ in range(int(stdin.readline().rstrip())):
    for _ in range(int(stdin.readline().rstrip())):
      stdout.write(str("="))
    stdout.write(str("\n"))


if __name__ == "__main__":
  main()
