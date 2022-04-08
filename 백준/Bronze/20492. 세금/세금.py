from sys import stdin, stdout


def main():
  N = int(stdin.readline().strip())
  # N, T, C, P = map(int, stdin.readline().strip().split())

  print(str(int(N * 0.78)) + " " + str( int(N * 0.8 + N*0.2*0.78) ))


if __name__ == "__main__":
  main()
