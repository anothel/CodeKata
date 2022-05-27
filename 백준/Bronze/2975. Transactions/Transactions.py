from sys import stdin, stdout


def solve():
  while True:
    cur, w, val = map(str, stdin.readline().rstrip().split())
    if w == "W" and int(cur) == 0 and int(val) == 0:
      break

    if w == "W":
      if int(cur) - int(val) < -200:
        stdout.write("Not allowed\n")
        continue
      stdout.write("%d\n" % (int(cur) - int(val)))
    else:
      if int(cur) + int(val) < -200:
        stdout.write("Not allowed\n")
        continue
      stdout.write("%d\n" % (int(cur) + int(val)))


if __name__ == "__main__":
    solve()
