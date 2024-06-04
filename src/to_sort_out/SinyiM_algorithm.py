numbers = [1,2,56,32,51,2,8,92,58]
print(numbers)
for i in range(1,len(numbers)-1):
    for j in range(i+1,len(numbers)):
        if numbers[i] > numbers[j]:
            temp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = temp
print(numbers)