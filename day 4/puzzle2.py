with open('input.txt') as input:
    lines = input.readlines()

sum = 0

for line in lines:
    number_interval1 = set([])
    number_interval2 = set([])
    isOverlaping = False
    
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
    
    for number in number_interval1:
        if number in number_interval2:
            isOverlaping = True
    
    if isOverlaping:
        sum += 1

print(sum)