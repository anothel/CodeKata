from sys import stdin, stdout


def solve():
  while True:
    lSentence: list = list(stdin.readline().rstrip())
    if len(lSentence) == 1 and lSentence[0] == ".":
      return

    lStack: list = list()
    lStack2: list = list()
    for token in lSentence:
      if token == "(" or token == "[" or token == "]" or token == ")":
        lStack.append(token)

    if len(lStack) == 0:
      stdout.write("yes\n")
      continue

    bPass: bool = True
    while lStack:
      tok: str = lStack.pop()
      if tok == "(":
        if len(lStack2) == 0:
          bPass = False
          break
        tmp: str = lStack2.pop()
        if tmp != ")":
          bPass = False
          break
      elif tok == "[":
        if len(lStack2) == 0:
          bPass = False
          break
        tmp: str = lStack2.pop()
        if tmp != "]":
          bPass = False
          break
      elif tok == ")" or tok == "]":
        lStack2.append(tok)

    if bPass == True and len(lStack2) == 0:
      stdout.write("yes\n")
    else:
      stdout.write("no\n")


if __name__ == "__main__":
    solve()
