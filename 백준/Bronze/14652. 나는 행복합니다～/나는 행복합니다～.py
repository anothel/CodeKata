from sys import stdin, stdout


def main():
  N, M, K = map(int, stdin.readline().strip().split())
  print(str(K//M) + " " + str(K % M))


if __name__ == "__main__":
    main()
