def detect_marker(line):

    i = 0

    while i <= len(line):
        theres_equal = False

        code = ''

        for index in range(14):
            if (i+index <= len(line)):
                code += line[i+index]
        
        for letter in code:
            if code.count(letter) > 1:
                theres_equal = True

        if (theres_equal):
            i += 1
        else:
            return i+14
            

with open('input.txt') as input:
    lines = input.readlines()

for line in lines:
    print(detect_marker(line))


