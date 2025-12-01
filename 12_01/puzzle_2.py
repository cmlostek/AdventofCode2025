with open('input.txt', 'r') as file:
    rotations = file.readlines()
dial = 50
password = 0

for item in rotations:
    idx = rotations.index(item)
    item = item.strip('\n')
    rotations[idx] = item

print(rotations)

for rotate in rotations:
    if rotate[0] == 'R':
        old_dial = dial
        dial += int(rotate[1:])
        for i in range(old_dial + 1, dial + 1):
            if i % 100 == 0:
                password += 1
        dial = dial % 100
        print(dial)
    elif rotate[0] == 'L':
        old_dial = dial
        dial -= int(rotate[1:])
        for i in range(old_dial - 1, dial - 1, -1):
            if i % 100 == 0:
                password += 1
        dial = dial % 100
        print(dial)

print("password is: ", password)

