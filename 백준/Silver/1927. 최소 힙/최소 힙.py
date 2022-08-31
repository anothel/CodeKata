from sys import stdin, stdout
import heapq


def solution():
    queue: heapq = []
    for _ in range(int(stdin.readline().rstrip())):
        n: int = int(stdin.readline().rstrip())

        if n == 0:
            if len(queue) == 0:
                stdout.write("0\n")
            else:
                stdout.write("%d\n" % heapq.heappop(queue))
        else:
            heapq.heappush(queue, n)


if __name__ == "__main__":
    solution()
