from sys import stdin, stdout
import datetime


def main():
  limit = int(stdin.readline().strip())
  speed = int(stdin.readline().strip())

  current = speed - limit
  fine: int = 0
  if 1 <= current and current <= 20:
    fine = 100
  elif 21 <= current and current <= 30:
    fine = 270
  elif 31 <= current:
    fine = 500

  if fine == 0:
    print("Congratulations, you are within the speed limit!")
  else:
    print("You are speeding and your fine is $%d." % fine)


if __name__ == "__main__":
  main()
