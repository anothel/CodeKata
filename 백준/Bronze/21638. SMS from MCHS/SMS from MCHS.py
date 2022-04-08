from sys import stdin, stdout


def main():
  t1, v1 = map(int, stdin.readline().rstrip().split())
  t2, v2 = map(int, stdin.readline().rstrip().split())

  if t2 < 0 and 10 <= v2:
    stdout.write(
        "A storm warning for tomorrow! Be careful and stay home if possible!")
  elif t2 < t1:
    stdout.write("MCHS warns! Low temperature is expected tomorrow.")
  elif v1 < v2:
    stdout.write("MCHS warns! Strong wind is expected tomorrow.")
  else:
    stdout.write("No message")


if __name__ == "__main__":
  main()
