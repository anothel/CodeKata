from sys import stdin, stdout


def main():
  n = int(stdin.readline().strip())
  k = int(stdin.readline().strip())
  
  h = k + 60
  
  
  if n > h:
    n = h * 1500 + (n - h) * 3000
  else:
    n *= 1500
  
  stdout.write(str(n))



if __name__ == "__main__":
    main()
