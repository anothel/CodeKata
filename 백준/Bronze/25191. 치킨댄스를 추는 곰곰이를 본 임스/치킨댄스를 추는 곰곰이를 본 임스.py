from sys import stdin, stdout


def solve():
    nChickenCount:int =  int(stdin.readline().strip())
    nCoke, nBeer = map(int, stdin.readline().strip().split())
    nAnswer:int = nCoke//2 + nBeer
    if nAnswer > nChickenCount:
        nAnswer = nChickenCount
    stdout.write("%d\n" % nAnswer)


if __name__ == "__main__":
    solve()
