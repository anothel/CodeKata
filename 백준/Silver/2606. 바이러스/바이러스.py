from sys import stdin
from collections import deque


if __name__ == "__main__":
    computerCnt = int(stdin.readline().strip())
    networkCnt = int(stdin.readline().strip())

    graph = [[] for _ in range(computerCnt + 1)]
    for _ in range(networkCnt):
        c1, c2 = map(int, stdin.readline().split())
        graph[c1].append(c2)
        graph[c2].append(c1)

    visited = [False] * (computerCnt + 1)
    q = deque()
    q.append(1)
    visited[1] = True
    infected = 0

    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                infected += 1
                q.append(nxt)
    print(infected)
