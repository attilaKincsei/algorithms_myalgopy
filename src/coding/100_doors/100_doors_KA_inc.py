"""The Problem
You have 100 doors in a hallway in a row that are all
initially closed. You make 100 passes by the doors.
The first time through, you visit every door and toggle
the door (if the door is closed, you open it;
if it is open, you close it). The second time you only
visit every 2nd door (door #2, #4, #6, ...).
The third time, every 3rd door (door #3, #6, #9, ...), etc,
until you only visit the 100th door.

Description
Write a script that lists the number (the name)
of the open doors after you visited all the 100 doors 100 a times.
This is an individual assignment but of course,
you can get help from the others.
https://codecool.instructure.com/courses/74/assignments/2491?module_item_id=15623
"""


## solultion
# trying out new codes for 100_doors

"""The Problem
You have 100 doors in a hallway in a row that are all
initially closed. You make 100 passes by the doors.
The first time through, you visit every door and toggle
the door (if the door is closed, you open it;
if it is open, you close it). The second time you only
visit every 2nd door (door #2, #4, #6, ...).
The third time, every 3rd door (door #3, #6, #9, ...), etc,
until you only visit the 100th door.

Description
Write a script that lists the number (the name)
of the open doors after you visited all the 100 doors 100 a times.
This is an individual assignment but of course,
you can get help from the others."""


## solultion


# creating the list
doors_orig = [1]
for i in range(99):
    doors_orig.append(1)

print(len(doors_orig))
print(doors_orig)


# toggling with a fun
def hund_door(x, numtog):
    for i in range(0, 100, numtog):
        x[i] = x[i] * -1

print(len(doors_orig))
print(doors_orig)

numtog = 1
while numtog <= 100:
    hund_door(doors_orig, numtog = numtog)
    numtog += 1

print(doors_orig)

# closed = 1
# open = -1


print(doors_orig.count(-1))
print(doors_orig.index(-1))

for i in range(100):
    if doors_orig[i] == -1:
        print(i)

## problem to solve: 100 stayed closed.
# sol: change starting point to 1 from 0 when doing the 2nd iteration.