from sys import stdin, stdout


def main():

  n, w, h, l = map(int, stdin.readline().rstrip().split())
  
  stdout.write(str( n if  n <  (w//l) *  (h//l) else (w//l) *  (h//l) ))


if __name__ == "__main__":
    main()
