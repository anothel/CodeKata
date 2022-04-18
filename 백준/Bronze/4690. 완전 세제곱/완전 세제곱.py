from sys import stdin, stdout


def solution():
  for a in range(6, 101):
    for b in range(2, a+1):
      if b > a:
        break
      for c in range(b, a+1):
        if c > a:
          break
        for d in range(c, a+1):
          if d > a:
            break
          if a*a*a == b*b*b + c*c*c + d*d*d:
            stdout.write("Cube = %d, Triple = (%d,%d,%d)\n" % (a, b, c, d))
          elif a*a*a < b*b*b + c*c*c + d*d*d:
            break


if __name__ == "__main__":
    solution()
