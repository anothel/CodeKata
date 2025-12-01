from sys import stdin


def solution(s):
    if s >= 620 and s <= 780:
        print('Red')
    elif s >= 590 and s < 620:
        print('Orange')
    elif s >= 570 and s < 590:
        print('Yellow')
    elif s >= 495 and s < 570:
        print('Green')
    elif s >= 450 and s < 495:
        print('Blue')
    elif s >= 425 and s < 450:
        print('Indigo')
    elif s >= 380 and s < 425:
        print('Violet')


if __name__ == "__main__":
    s = int(stdin.readline().strip())
    solution(s)
