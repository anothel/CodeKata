from sys import stdin, stdout


def solve():
  a, b = map(int, stdin.readline().rstrip().split())
  c, d = map(int, stdin.readline().rstrip().split())

  nums: list = [a/c+b/d,
                c/d+a/b,
                d/b+c/a,
                b/a+d/c]

  stdout.write(str(nums.index(max(nums))))


def main():
  solve()


if __name__ == "__main__":
    main()
