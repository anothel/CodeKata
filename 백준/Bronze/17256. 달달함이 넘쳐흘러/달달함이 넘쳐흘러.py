from sys import stdin, stdout


def main():
  ax, ay, az = map(int, stdin.readline().strip().split())
  cx, cy, cz = map(int, stdin.readline().strip().split())

  print(str(cx - az) + " " + str(cy // ay) + " " + str(cz - ax))


if __name__ == "__main__":
    main()
