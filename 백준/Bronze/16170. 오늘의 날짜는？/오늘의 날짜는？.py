from sys import stdin, stdout
import time


def main():
  now = time.localtime()
  print(now.tm_year)
  print(now.tm_mon)
  print(now.tm_mday)



if __name__ == "__main__":
    main()
