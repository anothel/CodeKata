from sys import stdin, stdout


def solve():
  people: list = list()

  for _ in range(int(stdin.readline().rstrip())):
    n, d, m, y = map(str, stdin.readline().rstrip().split())
    people.append([n, int(d), int(m), int(y)])
  people.sort(key=lambda x:(x[3], x[2], x[1]))

  stdout.write("%s\n" % people[-1][0])
  stdout.write("%s\n" % people[0][0])


if __name__ == "__main__":
    solve()
