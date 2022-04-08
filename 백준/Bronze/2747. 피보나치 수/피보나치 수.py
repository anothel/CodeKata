from sys import stdin, stdout


def main():
  n = int(stdin.readline().strip())
  fi: list = list(0 for _ in range(47))

  fi[0] = 0
  fi[1] = 1
  for i in range(n):
    fi[i + 2] = fi[i] + fi[i+1]

  stdout.write(str(fi[n]))


if __name__ == "__main__":
    main()
