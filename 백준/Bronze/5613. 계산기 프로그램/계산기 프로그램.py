from sys import stdin, stdout


def solution():
  nCurNumber: int = int(stdin.readline().rstrip())
  sCurOperator: str = ""
  while True:
    input: str = stdin.readline().rstrip()
    if input == "=":
      break

    if input.isdigit():
      if sCurOperator == "+":
        nCurNumber += int(input)
      elif sCurOperator == "-":
        nCurNumber -= int(input)
      elif sCurOperator == "*":
        nCurNumber *= int(input)
      elif sCurOperator == "/":
        nCurNumber //= int(input)
    else:
      sCurOperator = input
  stdout.write("%d\n" % nCurNumber)


if __name__ == "__main__":
  solution()
