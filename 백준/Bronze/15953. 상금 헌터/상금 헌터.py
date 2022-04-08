from sys import stdin, stdout


  # a, b = map(int, stdin.readline().rstrip().split())
  # n = int(stdin.readline().rstrip())
def main():
  for _ in range(int(stdin.readline().rstrip())):
    sum: int = 0
    a, b = map(int, stdin.readline().rstrip().split())
      
    if a == 0:
      sum = 0
    elif a == 1:
      sum += 5000000
    elif a > 1 and a <= 3:
      sum += 3000000
    elif a > 3 and a <= 6:
      sum += 2000000
    elif a > 6 and a <= 10:
      sum += 500000
    elif a > 10 and a <= 15:
      sum += 300000
    elif a > 15 and a <= 21:
      sum += 100000

    if b == 0:
      sum += 0
    elif b == 1:
      sum += 5120000
    elif b > 1 and b <= 3:
      sum += 2560000
    elif b > 3 and b <= 7:
      sum += 1280000
    elif b > 7 and b <= 15:
      sum += 640000
    elif b > 15 and b <= 31:
      sum += 320000
    
    stdout.write(str(sum) + "\n")


if __name__ == "__main__":
  main()
