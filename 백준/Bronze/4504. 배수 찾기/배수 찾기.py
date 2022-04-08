from sys import stdin, stdout


def main():
  n = int(stdin.readline().rstrip())
  while True:    
    a = int(stdin.readline().rstrip())
    if a == 0:
      break;
    if a % n == 0:
      stdout.write(str(a) + " is a multiple of " + str(n) + ".\n")
    else:
      stdout.write(str(a) + " is NOT a multiple of " + str(n) + ".\n")
  

if __name__ == "__main__":
  main()
