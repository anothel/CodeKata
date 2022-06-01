from sys import stdin, stdout


def solve():
  check: list = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
  for _ in range(int(stdin.readline().rstrip())):
    sentence: str = stdin.readline().rstrip().replace(" ", "")
    vowels: int = 0
    for s in check:
      vowels += sentence.count(s)

    stdout.write("%d %d\n" % (len(sentence) - vowels, vowels))


if __name__ == "__main__":
    solve()
