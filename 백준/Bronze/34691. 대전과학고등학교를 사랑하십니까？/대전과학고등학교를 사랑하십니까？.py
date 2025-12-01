from sys import stdin


def solution(s):
    if s == 'animal':
        print('Panthera tigris')
    elif s == 'flower':
        print('Forsythia koreana')
    elif s == 'tree':
        print('Pinus densiflora')


if __name__ == "__main__":
    while True:
        s = (stdin.readline().strip())
        if s == 'end':
            break
        solution(s)
