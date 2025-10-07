def absVal(x):
    if (x < 0):
        x *= -1
    return x

def main():
    x = int(input("Please input a number:"))
    print(absVal(x))

main()
