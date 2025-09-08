import random

# Get user input for levels and amount
print("Levels?")
levels = input().split(',')
total = 0
select = []
for level in levels:
    level = level.strip()
    print(f"Amount from {level}?")
    amount = int(input())

    # Load file lists into arrays
    arr = []
    file = open(f"{level}.txt", "r", encoding='utf8')
    lines = file.read().splitlines()
    for line in lines:
        arr.append(line.strip())
    file.close()

    # Extract random entries
    used = []
    for entry in range(0, amount):
        i = random.randint(0, len(arr)-1)
        while i in used or arr[i][0] == '#':
            i = random.randint(1, len(arr))   
        select.append([arr[i], level])
        used.append(i)

# Display selected items
print("Selection:")
i = 1
for item in select:
    print(str(i) + '. ' + item[0] + ' [' + item[1] + ']')
    i += 1

while True:
    print("Mark?")
    opt = input()
    if opt == '':
        break

    opt = opt.split(',')
    for index in opt:
        index = int(index)
        arr = []
        # Go to file and prefix with #
        file = open(f"{select[index - 1][1]}.txt", "r", encoding='utf8')
        lines = file.read().splitlines()
        for line in lines:
            if line.strip() == select[index - 1][0]:
                lines[lines.index(select[index - 1][0])] = "#" + select[index - 1][0]
            arr.append(line.strip())
        file.close()

        # Write file with marks
        file = open(f"{select[index - 1][1]}.txt", "w", encoding='utf8')
        for line in lines:
            file.write(line + '\n')
        file.close()

        # Generate a replacement grammar point
        i = random.randint(0, len(arr)-1)
        subset = [item[0] for item in select]
        while arr[i] in subset or arr[i][0] == '#':
            i = random.randint(1, len(arr))
        # Replace at index to avoid interfering with further marks  
        level = select[index - 1][1]; 
        select.pop(index-1)
        select.insert(index-1, [arr[i], level])

    print("Selection:")
    i = 1
    for item in select:
        print(str(i) + '. ' + item[0] + ' [' + item[1] + ']')
        i += 1


