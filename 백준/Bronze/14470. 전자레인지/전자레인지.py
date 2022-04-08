from sys import stdin, stdout


def main():

  # stdout.write(
  #     str("%.15f" % float((int(stdin.readline().rstrip()) ** 2) * 3 ** 0.5 / 4)))
  A: int = int(stdin.readline().rstrip())
  B: int = int(stdin.readline().rstrip())
  C: int = int(stdin.readline().rstrip())
  D: int = int(stdin.readline().rstrip())
  E: int = int(stdin.readline().rstrip())
  
  waste_time: int = 0
  if A < 0 : 
    time_to_zero = (0 - A)*C + D
    zero_to_target =  B * E
    waste_time  = time_to_zero + zero_to_target
  elif A == 0 :
    waste_time = D + B*E
  else :
    waste_time = (B-A)*E
  
  stdout.write(str(waste_time))
  


if __name__ == "__main__":
    main()
