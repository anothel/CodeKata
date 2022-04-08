from sys import stdin, stdout


def main():
  h1, m1, s1 = map(int, stdin.readline().rstrip().split(" : "))
  h2, m2, s2 = map(int, stdin.readline().rstrip().split(" : "))

  h1 = h1 * 3600 + m1 * 60 + s1
  h2 = h2 * 3600 + m2 * 60 + s2
  diff = h2 - h1

  stdout.write(str(diff if h1 < h2 else diff + 24*3600))
  # nums = list(map(int, stdin.readline().rstrip().split()))
  # stdout.write(str("1" if nums.count(2) < nums.count(1) else "2"))


if __name__ == "__main__":
  main()
