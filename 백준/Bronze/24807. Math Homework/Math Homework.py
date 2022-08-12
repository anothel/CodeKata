from sys import stdin, stdout


def getLegsCount(b: int, d: int, c: int, i: int, j: int, k: int) -> int:
    return b * i + d * j + c * k


if __name__ == "__main__":
    b, d, c, l = map(int, stdin.readline().rstrip().split())

    isPossible: bool = False
    for i in range(251):
        for j in range(251):
            for k in range(251):
                current: int = b * i + d * j + c * k
                # current: int = getLegsCount(b, d, c, i, j, k)
                if current == l:
                    stdout.write("%d %d %d\n" % (i, j, k))
                    isPossible = True
                    break
                elif current < l:
                    continue
                elif current > l:
                    break

    if isPossible == False:
        stdout.write("impossible\n")
