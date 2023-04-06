from sys import stdin, stdout


def printHeart():
    stdout.write(" @@@   @@@ \n")
    stdout.write("@   @ @   @\n")
    stdout.write("@    @    @\n")
    stdout.write("@         @\n")
    stdout.write(" @       @ \n")
    stdout.write("  @     @  \n")
    stdout.write("   @   @   \n")
    stdout.write("    @ @    \n")
    stdout.write("     @     \n")
    return


def solution():

    n: int = int(stdin.readline().strip())
    for _ in range(n):
        printHeart()


if __name__ == "__main__":
    solution()
