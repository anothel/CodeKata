from sys import stdin, stdout


def main():
  br, bc = map(int, stdin.readline().rstrip().split())
  dr, dc = map(int, stdin.readline().rstrip().split())
  jr, jc = map(int, stdin.readline().rstrip().split())

  d = abs(dr - jr) + abs(dc - jc)
  b = max(abs(br - jr), abs(bc - jc))

  if d < b:
    stdout.write(str("daisy"))
  elif b < d:
    stdout.write(str("bessie"))
  else:
    stdout.write(str("tie"))


if __name__ == "__main__":
    main()
