#Sorting algo - RA CC Python SI1 A3
import re

#getting the number from the user:
input_numbers = []
input_numbers = input("\nTell me positive integers that you want to sort, by separting them with a coma (so for example: 10,2,45):\n\n")
#exception handler for wrong format:  
while True:
    if (len(input_numbers)<6 or len(input_numbers)>100):
        input_numbers = input("Wrong format!\nTell me the numbers that you want to sort, by separting them with a coma (so for example: 10,2,45)\n: ")
    elif re.search("[a-z]",input_numbers):
        input_numbers = input("Wrong format!\nTell me the numbers that you want to sort, by separting them with a coma (so for example: 10,2,45)\n: ")
    elif not re.search("[,]",input_numbers):
        input_numbers = input("Wrong format!\nTell me the numbers that you want to sort, by separting them with a coma (so for example: 10,2,45)\n: ")
    else:
        break
input_numbers = input_numbers.split(",")
print("\nYou gave these numbers:\n") 
print(*input_numbers, sep=',')
input_numbers = list(map(int, input_numbers)) 

#the actual sorting starts here:
def sorting():
    iteration = 1
    N = len(input_numbers)
    
    while iteration < N:
        j = 0
        while j <= N-2:
            if input_numbers[j] > input_numbers [j+1]:
                temp = input_numbers[j+1]
                input_numbers[j+1] = input_numbers[j]
                input_numbers[j] = temp 
            else: 
                j += 1     
        else:
            iteration += 1         

sorting() 
print("\nSorted numbers:\n") 
print(*input_numbers, sep=',')
print("")

    
