from sys import stdin, stdout

# BMI = 체중/(신장 × 신장)

def solution():
    w: float = float(stdin.readline().rstrip())
    h: float = float(stdin.readline().rstrip())
    a = w / (h * h)

    if a < 18.5:
        stdout.write("Underweight\n")
    elif 18.5 <= a and a <= 25:
        stdout.write("Normal weight\n")
    else:
        stdout.write("Overweight\n")


if __name__ == "__main__":
    solution()
