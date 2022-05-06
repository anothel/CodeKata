from sys import stdin, stdout


def solve():
  for _ in range(int(stdin.readline().rstrip())):
    nInput: int = int(stdin.readline().rstrip())
    if bin(int(bin(nInput), 2) & int(bin(-nInput), 2)) == bin(nInput):
      stdout.write("1\n")
    else:
      stdout.write("0\n")


if __name__ == "__main__":
    solve()
