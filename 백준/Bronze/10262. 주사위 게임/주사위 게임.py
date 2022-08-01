from sys import stdin, stdout


def solve():
    a1, b1, a2, b2 = map(int, stdin.readline().rstrip().split())
    a3, b3, a4, b4 = map(int, stdin.readline().rstrip().split())
    Gunnar: int = a1 + b1 + a2 + b2
    Emma: int = a3 + b3 + a4 + b4
    if Gunnar > Emma:
        stdout.write("Gunnar\n")
    elif Emma > Gunnar:
        stdout.write("Emma\n")
    else:
        stdout.write("Tie\n")


if __name__ == "__main__":
    solve()
