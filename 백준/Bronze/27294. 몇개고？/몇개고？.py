from sys import stdin, stdout


def solution():
    t, s = map(int, stdin.readline().rstrip().split())

    isLunch: bool = False
    isAhlcohol: bool = False

    if t >= 12 and t <= 16:
        isLunch = True
    if s == 1:
        isAhlcohol = True

    if isAhlcohol == True or isLunch == False:
        stdout.write("280\n")
    elif isAhlcohol == False and isLunch == True:
        stdout.write("320\n")
    else:
        stdout.write("320\n")


if __name__ == "__main__":
    solution()
