from sys import stdin, stdout


def main():
  a: list = list()
  a.append(int(stdin.readline().strip()))
  a.append(int(stdin.readline().strip()))
  a.append(int(stdin.readline().strip()))

  print("The 1-3-sum is " + str(9*1 + 7*3 + 8*1 + 0*3 + 9*1 + 2*3 + 1*1 +
        4*3 + 1*1 + 8*3 + a[0]*1 + a[1]*3 + a[2]*1))


if __name__ == "__main__":
  main()
