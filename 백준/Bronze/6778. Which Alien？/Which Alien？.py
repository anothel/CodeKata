from sys import stdin, stdout


def main():
  antenna:int =  int(stdin.readline().strip())
  eyes:int =  int(stdin.readline().strip())
  
  if 3 <= antenna and eyes <=4:
    print("TroyMartian")
  if antenna <= 6 and 2 <= eyes:
    print("VladSaturnian")
  if antenna <= 2 and eyes <= 3:
    print("GraemeMercurian")


if __name__ == "__main__":
  main()
