
print("""Hello!
I am a code that sorts lists of numbers in ascending order
\n- Give me one integer number at every prompt.
- Use only the digits from 0 to 9.
- Enter 's' to start sorting.
- Enter 'q' to quit the program.
- Enter 'h' to display instructions again.""")

inp = None
linp = []
linp_boo = []
OrigNumbers = []
numbers = []
N = None
print("L16 original list:", OrigNumbers) # del
while True:
    inp = input("Enter an integer: ")
    linp = list(inp)
    for i in range(len(linp)):
        linp_boo = linp
        linp_boo[i] = linp[i] in list("0123456789")
    if inp == "q":
        print("You quit the program.")
        print("L25 original list:", OrigNumbers) # del
        break
    elif inp == "h":
        print("""- Give me one integer number at every prompt.
        - Use only the digits from 0 to 9.
        - Enter 's' to start sorting.
        - Enter 'q' to quit the program.
        - Enter 'h' to display instructions again.""")
    elif inp == "s":
        print("L34 original list:", OrigNumbers) # print orig  list here, if you want to keep its order
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
        print("L49 This was your original list:", OrigNumbers) # BUG !!!: already ascending order!!!
        print("This is your list in ascending order:", numbers)
        OrigNumbers = []
        print("L55 original list:", OrigNumbers) # del
        numbers = []
    elif False not in linp_boo:
        OrigNumbers.append(int(inp))
        print("This is your list so far:", OrigNumbers) # del
    else:
        print("\nYou entered: ", inp, "\n\nThis is not an integer\nTry again or quit.\n")



