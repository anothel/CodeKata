from sys import stdin, stdout
from collections import deque


def solve():
    scores: deque = deque(stdin.readline().rstrip())
    scoreA: int = 0
    scoreB: int = 0
    while scores:
        person: str = scores.popleft()
        if person == "A":
            scoreA += int(scores.popleft())
        elif person == "B":
            scoreB += int(scores.popleft())
    stdout.write("A" if scoreA > scoreB else "B")


if __name__ == "__main__":
    solve()
