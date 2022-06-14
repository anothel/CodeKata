from sys import stdin, stdout


def solution():
  words: list = [0] * 26
  s: list = list(stdin.readline().rstrip())
  for i in s:
    words[ord(i)-97] += 1

  for i in words:
    stdout.write("%d " % i)


if __name__ == "__main__":
  solution()
