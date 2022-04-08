from sys import stdin, stdout


def main():
  for _ in range(int(stdin.readline())):
    hp, mp, power, amor, a, b, c, d = map(
        int, stdin.readline().rstrip().split())
    hp += a
    hp = 1 if hp < 1 else hp
    mp += b
    mp = 1 if mp < 1 else mp
    power += c
    power = 0 if power < 0 else power
    amor += d
    
    stdout.write(str(1*(hp) + 5 * (mp) + 2*(power)+2*(amor)) + "\n")


if __name__ == "__main__":
  main()
