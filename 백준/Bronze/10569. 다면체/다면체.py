from sys import stdin, stdout


def main():
  for _ in range(int(stdin.readline().strip())):
    v, e = map(int, stdin.readline().rstrip().split())

    stdout.write(str(2-v+e) + "\n")


if __name__ == "__main__":
    main()
