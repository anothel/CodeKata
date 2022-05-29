from sys import stdin, stdout


def solve():
  a, b = map(int, stdin.readline().rstrip().split())

  if a == b:
    stdout.write("0\n")
    return
  
  big, small = max(a, b), min(a, b)
  stdout.write("%d\n" % (big - small - 1))

  for i in range(small + 1, big):
    stdout.write("%d " % i)


if __name__ == "__main__":
    solve()
