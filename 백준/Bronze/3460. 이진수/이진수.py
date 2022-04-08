from sys import stdin, stdout


def main():
  for _ in range(int(stdin.readline().rstrip())):
    a = list(str(bin(int(stdin.readline().rstrip()))[2:]))
    a.reverse()

    for i in range(len(a)):
      if a[i] == '0':
        continue
      else:
        stdout.write(str(i) + " ")
    stdout.write(str("\n"))


if __name__ == "__main__":
  main()
