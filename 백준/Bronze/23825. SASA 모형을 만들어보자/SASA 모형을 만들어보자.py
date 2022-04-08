from sys import stdin, stdout


def main():
  # # n = int(stdin.readline().strip())
  # N, M = map(int, stdin.readline().strip().split())
  
  N = list(map(int, stdin.readline().strip().split()))
  print(min(N)//2)
    
  # N.sort()
  # for i in N:
  #   stdout.write(str(i) + " ")

  # if M == 1 or M == 2:
  #   stdout.write(str("NEWBIE!"))
  # elif M <= N:
  #   stdout.write(str("OLDBIE!"))
  # else:
  #   stdout.write(str("TLE!"))
  # print(abs(N-M))


if __name__ == "__main__":
  main()
