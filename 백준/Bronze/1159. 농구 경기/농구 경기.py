from sys import stdin, stdout


def solve():
    alpha: dict = {chr(i): 0 for i in range(97, 123)}

    for _ in range(int(stdin.readline().rstrip())):
        alpha[list(stdin.readline().rstrip())[0]] += 1
    checkPass: bool = False
    for check in alpha:
        if alpha[check] >= 5:
            stdout.write("%s" % check)
            checkPass = True
    if checkPass == False:
        stdout.write("PREDAJA\n")


if __name__ == "__main__":
    solve()
