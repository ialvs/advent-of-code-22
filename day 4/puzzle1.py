with open('input.txt') as input:
    lines = input.readlines()


sum = 0

for line in lines:
    number_interval1 = set([])
    number_interval2 = set([])
    
    intervals = line.split(',')
    i = int(intervals[0].split('-')[0])
    max = int(intervals[0].split('-')[1])
    
    while i <= max:
        number_interval1.add(i)
        i += 1
    
    i = int(intervals[1].split('-')[0])
    max = int(intervals[1].split('-')[1])
    
    while i <= max:
        number_interval2.add(i)
        i += 1
    
    if (number_interval1.issubset(number_interval2) or number_interval2.issubset(number_interval1)):
        sum += 1

print(sum)
