def sumEven(x):
    sum = 0

    for i in range(x+1):
        if (i % 2 == 0):
            sum += i
    return sum

def main():
    x = 12
    print(sumEven(x))

main()
        

