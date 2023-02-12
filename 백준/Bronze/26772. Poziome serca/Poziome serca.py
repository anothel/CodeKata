from sys import stdin, stdout


def solution():
    n: int = int(stdin.readline().rstrip())

    for _ in range(n):
        stdout.write(" @@@   @@@  ")
    stdout.write("\n")
    for _ in range(n):
        stdout.write("@   @ @   @ ")
    stdout.write("\n")
    for _ in range(n):
        stdout.write("@    @    @ ")
    stdout.write("\n")
    for _ in range(n):
        stdout.write("@         @ ")
    stdout.write("\n")
    for _ in range(n):
        stdout.write(" @       @  ")
    stdout.write("\n")
    for _ in range(n):
        stdout.write("  @     @   ")
    stdout.write("\n")
    for _ in range(n):
        stdout.write("   @   @    ")
    stdout.write("\n")
    for _ in range(n):
        stdout.write("    @ @     ")
    stdout.write("\n")
    for _ in range(n):
        stdout.write("     @      ")
    stdout.write("\n")


if __name__ == "__main__":
    solution()
