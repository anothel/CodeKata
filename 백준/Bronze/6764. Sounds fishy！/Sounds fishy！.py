from sys import stdin, stdout


def main():
  fishCan: list = list()
  for _ in range(4):
    fishCan.append(int(stdin.readline().strip()))

  if fishCan[0] == fishCan[1] == fishCan[2] == fishCan[3]:
    print("Fish At Constant Depth")
    return

  for i in range(3):
    if fishCan[i] < fishCan[i + 1]:
      if i == 2:
        print("Fish Rising")
        return
      continue
    else:
      if i != 0:
        print("No Fish")
        return        
      break

  for i in range(3):
    if fishCan[i + 1] < fishCan[i]:
      if i == 2:
        print("Fish Diving")
        return
      continue
    else:
      print("No Fish")
      return

  print("No Fish")


if __name__ == "__main__":
  main()
