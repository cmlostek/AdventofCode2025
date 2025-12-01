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
        dial += int(rotate[1:])
        dial = dial % 100
        if dial == 0:
            password += 1
        print(dial)
    elif rotate[0] == 'L':
        dial -= int(rotate[1:])
        dial = dial % 100
        if dial == 0:
            password += 1
        print(dial)

print("password is: ", password)

