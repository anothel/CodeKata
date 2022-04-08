from sys import stdin, stdout


def main():
  N, a, b = map(int, stdin.readline().strip().split())
  rows: list = list()
  for _ in range(N):
    rows.append(list(map(int, stdin.readline().strip().split())))

  result: str = "HAPPY"
  for i in range(N):
    if i == a-1:
      end: bool = False
      for j in range(N):
        if rows[i][j] > rows[a-1][b-1]:
          result = "ANGRY"
          end = True
          break
      if end == True:
        break
    elif rows[i][b-1] > rows[a-1][b-1]:
      result = "ANGRY"
      break

  stdout.write(str(result))


if __name__ == "__main__":
    main()
