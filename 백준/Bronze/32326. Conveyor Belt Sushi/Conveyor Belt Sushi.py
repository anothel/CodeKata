from sys import stdin


def solution(r,g,b):


    print(r*3+g*4+b*5)


if __name__ == "__main__":
    r = int(stdin.readline().strip())
    g = int(stdin.readline().strip())
    b = int(stdin.readline().strip())
    solution(r,g,b)
