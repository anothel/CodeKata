from sys import stdin, stdout


def solution():
    board: list = list(stdin.readline().rstrip())

    answer: str = ''

    countX: int = 0
    for i in board:
        if i == 'X':
            countX += 1
        elif i == '.':
            if countX % 2 == 1:
                stdout.write("-1\n")
                return
            if countX == 2:
                answer += 'BB'
                countX = 0
            answer += '.'
        if countX == 4:
            answer += 'AAAA'
            countX = 0
    if countX == 1 or countX == 3:
        stdout.write("-1\n")
    else:
        if countX == 2:
          answer += 'BB'
        stdout.write("%s\n" % answer)


if __name__ == "__main__":
    solution()
