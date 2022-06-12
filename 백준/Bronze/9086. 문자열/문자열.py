from sys import stdin, stdout


def solution():
  for _ in range(int(stdin.readline().rstrip())):
    word = list(stdin.readline().rstrip())
    stdout.write("%s%s\n" % (word[0], word[-1]))


if __name__ == "__main__":
  solution()
