from sys import stdin, stdout


def main():
  for _ in range(int(stdin.readline().rstrip())):
    s = int(stdin.readline().rstrip())
    for _ in range(int(stdin.readline().rstrip())):
      q, p = map(int, stdin.readline().rstrip().split())
      s += q*p
    stdout.write(str(s) + "\n")


if __name__ == "__main__":
  main()


