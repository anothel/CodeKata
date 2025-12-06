from sys import stdin

if __name__ == "__main__":
    t = int(stdin.readline().strip())
    for _ in range(t):
        n = int(stdin.readline().strip())
        c = {}

        for _ in range(n):
            name, category = stdin.readline().strip().split()
            if category in c:
                c[category] += 1
            else:
                c[category] = 1

        answer = 1
        for cnt in c.values():
            answer *= (cnt + 1)

        answer -= 1
        print(answer)
