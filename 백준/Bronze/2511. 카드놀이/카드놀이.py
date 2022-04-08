from sys import stdin, stdout


def main():
  playerA = list(map(int, stdin.readline().rstrip().split()))
  playerB = list(map(int, stdin.readline().rstrip().split()))
  scoreA: int = 0
  scoreB: int = 0
  isLastA: bool = False
  isLastB: bool = False
  for i in range(10):
    if playerA[i] > playerB[i]:
      scoreA += 3
      isLastA = True
      isLastB = False
    elif playerB[i] > playerA[i]:
      scoreB += 3
      isLastB = True
      isLastA = False
    else:
      scoreA += 1
      scoreB += 1

  stdout.write(str(scoreA) + " " + str(scoreB) + "\n")

  if scoreA > scoreB:
    stdout.write(str("A"))
  elif scoreB > scoreA:
    stdout.write(str("B"))
  else:
    if isLastA == False and isLastB == False:
      stdout.write(str("D"))
    else:
      stdout.write(str("A" if isLastA else "B"))


if __name__ == "__main__":
  main()
