#Original:
doors = []
for i in range(100):
    doors.append("closed")
print(doors)

for i in range(100):
    for x in range(0, 99, i+1):
        if doors[x] == "closed":
            doors[x] = "open"
        else:
            doors[x] = "closed"

print("Range step:", i+1)
print(doors)

# SHORTER alternative:
doors = [False] * 100
for i in range(100):
   for j in range(i, 100, i+1):
       doors[j] = not doors[j]
   print("Door %d:" % (i+1), 'open' if doors[i] else 'close')