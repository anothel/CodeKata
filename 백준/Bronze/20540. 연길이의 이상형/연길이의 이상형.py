from sys import stdin, stdout


def changer(s: str) -> str:
  if s == "E":
    return "I"
  elif s == "S":
    return "N"
  elif s == "T":
    return "F"
  elif s == "J":
    return "P"
  elif s == "I":
    return "E"
  elif s == "N":
    return "S"
  elif s == "F":
    return "T"
  elif s == "P":
    return "J"


def solve():
  mbti: list = list(stdin.readline().rstrip())
  for i in range(len(mbti)):
    stdout.write("%s" % changer(mbti[i]))


if __name__ == "__main__":
    solve()
