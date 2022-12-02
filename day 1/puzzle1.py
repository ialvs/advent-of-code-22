with open('input.txt') as input:
    lines = input.readlines()
    #print(lines)
    
lines_f = []

for l in lines:
    f = l.split('\n')
    lines_f.append(f[0])

#print(lines_f)

index = 0
sums = []
sum = 0

lines_f.append('')

for l in lines_f:
    if (l == ''):
        sums.append(sum)
        sum = 0
        index += 1
    else:
        sum += float(l)

sums.sort(reverse=True)
print(sums[0])