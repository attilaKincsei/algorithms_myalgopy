
print("Hello!")
print("I am a code that sorts lists of numbers in ascending order.")
print("Give me one integer number at every prompt.")
print("Use only digits from 0 to 9.")
print("Enter 's' to start sorting.")
print("Enter 'q' to quit the program.")
inp = None
linp = []
linp_boo = []
OrigNumbers = []
numbers = []
N = None
while True:
    inp = input("Enter an integer: ")
    linp = list(inp)
    for i in range(len(linp)):
        linp_boo = linp
        linp_boo[i] = linp[i] in list("0123456789")
    if inp == "q":
        print("You quit the program.")
        break
    elif inp == "s":
        numbers = OrigNumbers
        N = len(numbers)
        iterations = 1
        while iterations < N:
            j = 0
            while j <= N - 2:
                if numbers[j] > numbers[j + 1]:
                    temp = numbers[j + 1]
                    numbers[j + 1] = numbers[j]
                    numbers[j] = temp
                    j = j + 1
                else:
                    j = j + 1
            iterations = iterations + 1
        print("This was your original list:", OrigNumbers)
        print("This is your list in ascending order:", numbers)
        OrigNumbers = []
        numbers = []
    elif False not in linp_boo:
        OrigNumbers.append(int(inp))
    else:
        print("\nYou entered: ", inp, "\n\nThis is not an integer\nTry again or quit.\n")


