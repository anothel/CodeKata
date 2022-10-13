from sys import stdin, stdout


def solution():
    e, f, c = map(int, stdin.readline().rstrip().split())

    myBottle: int = e + f

    drink: int = 0
    answer: int = 0

    while myBottle // c > 0:
        drink += myBottle // c
        answer = myBottle // c
        myBottle = myBottle % c + answer

    stdout.write("%d\n" % drink)


if __name__ == "__main__":
    solution()