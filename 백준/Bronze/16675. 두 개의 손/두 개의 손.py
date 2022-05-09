from sys import stdin, stdout


def solve():
  lHands: list = list(map(str, stdin.readline().rstrip().split()))
  if lHands[0] != lHands[1] and lHands[2] != lHands[3]:
    stdout.write("?\n")
  elif lHands[0] == lHands[1] and lHands[2] != lHands[3]:
    if lHands[0] == "R" and (lHands[2] == "P" or lHands[3] == "P"):
      stdout.write("TK\n")
    elif lHands[0] == "S" and (lHands[2] == "R" or lHands[3] == "R"):
      stdout.write("TK\n")
    elif lHands[0] == "P" and (lHands[2] == "S" or lHands[3] == "S"):
      stdout.write("TK\n")
    else:
      stdout.write("?\n")
  elif lHands[2] == lHands[3] and lHands[0] != lHands[1]:
    if lHands[2] == "R" and (lHands[0] == "P" or lHands[1] == "P"):
      stdout.write("MS\n")
    elif lHands[2] == "S" and (lHands[0] == "R" or lHands[1] == "R"):
      stdout.write("MS\n")
    elif lHands[2] == "P" and (lHands[0] == "S" or lHands[1] == "S"):
      stdout.write("MS\n")
    else:
      stdout.write("?\n")
  else:
    if lHands[0] == "R":
      if lHands[2] == "R":
        stdout.write("?\n")
      elif lHands[2] == "S":
        stdout.write("MS\n")
      elif lHands[2] == "P":
        stdout.write("TK\n")
    elif lHands[0] == "S":
      if lHands[2] == "R":
        stdout.write("TK\n")
      elif lHands[2] == "S":
        stdout.write("?\n")
      elif lHands[2] == "P":
        stdout.write("MS\n")
    elif lHands[0] == "P":
      if lHands[2] == "R":
        stdout.write("MS\n")
      elif lHands[2] == "S":
        stdout.write("TK\n")
      elif lHands[2] == "P":
        stdout.write("?\n")


if __name__ == "__main__":
    solve()
