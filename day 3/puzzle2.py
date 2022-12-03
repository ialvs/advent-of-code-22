def get_priority(character):
    
    if (character >= 'a' and character <= 'z'):
        return ord(character) - 96
    elif (character >= 'A' and character <= 'Z'):
        return ord(character) - 38

with open('input.txt') as input:
    lines = input.readlines()

groups = []
i = 1
x = -2

while i <= (len(lines)/3):
    big_string = ''
    big_string += lines[x + 2] + lines[x + 3] + lines[x + 4]
    groups.append(big_string)
    i += 1
    x += 3

#print(groups)

sum = 0

for group in groups:
    spliced = group.split('\n')
    set1 = set(spliced[0])
    set2 = set(spliced[1])
    set3 = set(spliced[2])

    for letter in set1:
        if (letter in set2) and (letter in set3):
            sum += get_priority(letter)

print(sum)
   
