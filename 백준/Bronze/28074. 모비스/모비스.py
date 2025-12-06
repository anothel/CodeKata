from sys import stdin


if __name__ == "__main__":
    s = (stdin.readline().strip())

    if "M" in s and "O" in s and "B" in s and "I" in s and "S" in s:
        print("YES")
    else:
        print("NO")
        
