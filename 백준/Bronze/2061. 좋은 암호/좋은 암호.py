from sys import stdin, stdout


def solution():
  k, l = map(int, stdin.readline().rstrip().rsplit())
  
  for i in range(2, l):
    if k % i == 0:
      stdout.write("BAD %d\n" % i)
      return
  stdout.write("GOOD\n")


if __name__ == "__main__":
  solution()
