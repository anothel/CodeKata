from sys import stdin, stdout


def main():
  pan: list = list()
  for _ in range(9):
    pan.append(list(map(int,stdin.readline().rstrip().split())))

  maxValue: int = 0
  row: int = 0
  col: int = 0
  for i in range(9):
    for j in range(9):
      if pan[i][j] > maxValue:
        maxValue = pan[i][j]
        row = i + 1
        col = j + 1

  stdout.write(str(maxValue) + "\n")
  stdout.write(str(row) + " " + str(col))


if __name__ == "__main__":
    main()
