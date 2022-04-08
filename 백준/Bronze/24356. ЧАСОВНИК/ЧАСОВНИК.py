from sys import stdin, stdout


def main():
  t1, m1, t2, m2 = map(int, stdin.readline().rstrip().split())

  m1 += t1 * 60
  m2 += t2 * 60

  if m2 < m1:
    m2 += 24*60

  stdout.write(str(m2 - m1) + " " + str((m2 - m1)//30))


if __name__ == "__main__":
    main()
