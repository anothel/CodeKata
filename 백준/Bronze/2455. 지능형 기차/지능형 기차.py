from sys import stdin, stdout


def main():
  people:list = list()
  beforeP:int = 0
  for _ in range(4):
    outP, inP = map(int, stdin.readline().strip().split())
    people.append(beforeP + inP -outP)
    beforeP = beforeP + inP -outP

  stdout.write(str(max(people)))


if __name__ == "__main__":
    main()
