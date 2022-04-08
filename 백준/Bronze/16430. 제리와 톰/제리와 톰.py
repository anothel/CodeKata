from sys import stdin, stdout


def main():
  A, B = map(int, stdin.readline().strip().split())

  print(str(B-A) + " " + str(B))


if __name__ == "__main__":
    main()
