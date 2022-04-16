from sys import stdin, stdout


def solution():
  for _ in range(int(stdin.readline().rstrip())):
    stdout.write("%d\n" %
                 sum(list(map(int, stdin.readline().rstrip().split()))))


if __name__ == "__main__":
    solution()
