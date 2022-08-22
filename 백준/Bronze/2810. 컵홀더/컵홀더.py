from sys import stdin, stdout


def drawSeat(seat: str) -> str:
    holder: str = ''
    isL: bool = False
    for i in seat:
        if isL == False:
            holder += '*'
            holder += i
            if i == 'L':
                isL = True
        else:
            holder += i
            isL = False
    holder += '*'

    return holder


def solution():
    n: int = int(stdin.readline().rstrip())
    seatWithHoder: str = drawSeat(stdin.readline().rstrip())
    answer: int = 0
    for i in seatWithHoder:
        if i == "*":
            answer += 1
    stdout.write("%d\n" % answer if answer < n else "%d\n" % n)


if __name__ == "__main__":
    solution()
