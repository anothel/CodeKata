from sys import stdin, stdout


def main():
  w, h = map(int, stdin.readline().strip().split())

  stdout.write(str( w + h - ((w **2 + h **2) **0.5)  ))


if __name__ == "__main__":
    main()
