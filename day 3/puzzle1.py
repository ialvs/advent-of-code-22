def get_priority(character):
    
    if (character >= 'a' and character <= 'z'):
        return ord(character) - 96
    elif (character >= 'A' and character <= 'Z'):
        return ord(character) - 38

with open('input.txt') as input:
    lines = input.readlines()

sum = 0

for line in lines:
    
    half = len(line)
    
    slice1 = slice(0,half//2)
    slice2 = slice(half//2,half)
    set1 = set(line[slice1])
    set2 = set(line[slice2])
    
    for letter in set1:
        if (letter in set2):
            sum += get_priority(letter)

print(sum)




