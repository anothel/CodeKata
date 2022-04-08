from sys import stdin, stdout


def main():
  # n = int(stdin.readline().strip())
  D, H, W = map(int, stdin.readline().strip().split())

  x = ((D**2) / (H*H+W*W)) ** 0.5

  stdout.write(str(int(H * x)) + " " + str(int(W * x)))


if __name__ == "__main__":
  main()
