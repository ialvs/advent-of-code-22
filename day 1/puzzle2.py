with open('input.txt') as input:
    lines = input.readlines()
    
lines_f = []

for l in lines:
    f = l.split('\n')
    lines_f.append(f[0])


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
print(sums[1])
print(sums[2],'\n')

total_sum = sums[0] + sums[1] + sums[2]

print(total_sum)