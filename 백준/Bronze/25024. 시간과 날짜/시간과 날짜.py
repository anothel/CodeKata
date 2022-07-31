from sys import stdin, stdout


def solve():
    for i in range(int(stdin.readline().rstrip())):
        x, y = map(int, stdin.readline().rstrip().split())
        stdout.write("Yes " if x <= 23 and y <= 59 else "No ")
        if x == 1 or x == 3 or x == 5 or x == 7 or x == 8 or x == 10 or x == 12:
            if 1 <= y and y <= 31:
                stdout.write("Yes\n")
            else:
                stdout.write("No\n")
        elif x == 4 or x == 6 or x == 9 or x == 11:
            if 1 <= y and y <= 30:
                stdout.write("Yes\n")
            else:
                stdout.write("No\n")
        elif x == 2:
            if 1 <= y and y <= 29:
                stdout.write("Yes\n")
            else:
                stdout.write("No\n")
        else:
            stdout.write("No\n")
        continue


if __name__ == "__main__":
    solve()
