
import time
print("Hello!\n")
time.sleep(2)
print("I am a code that sorts lists of numbers in ascending order.\n")
time.sleep(2)
print("Give me one integer number at every prompt.\n")
time.sleep(2)
print("Use only digits from 0 to 9, please.\n")
time.sleep(2)
inp = input("Give me an integer\n(or type 'q' to quit the program): ")
if inp == "q":
    print("You chose to quit the program")
else:
    inp = int(inp)
    numbers = [inp]
while type(inp) is int:
    inp = input("Give me an integer\n(or type 's' to get me start sorting\nor type 'q' to quit the program): ")
    if inp == "q":
        print("You chose to quit the program")
    elif inp == "s":
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
        print("\nYour list in ascending order:\n", numbers, "\n")
    else:
        inp = int(inp)
        numbers.append(inp)
print("Goodbye!\n")

