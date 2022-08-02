from sys import stdin, stdout


def solve():
    alpha: dict = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
        'h': 0,
        'i': 0,
        'j': 0,
        'k': 0,
        'l': 0,
        'm': 0,
        'n': 0,
        'o': 0,
        'p': 0,
        'q': 0,
        'r': 0,
        's': 0,
        't': 0,
        'u': 0,
        'v': 0,
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0
    }
    for _ in range(int(stdin.readline().rstrip())):
        name: list = list(stdin.readline().rstrip())
        alpha[name[0]] += 1
    checkPass: bool = False
    for check in alpha:
        if alpha[check] >= 5:
            stdout.write("%s" % check)
            checkPass = True
    if checkPass == False:
        stdout.write("PREDAJA\n")


if __name__ == "__main__":
    solve()
