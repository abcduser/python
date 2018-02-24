filename = input('Enter file name')

file = open(filename, 'r')

lines = []

for line in file:
    lines.append(line)

file.close()
print('No of lines are : {}'.format(len(lines)))

while True:
    l_no = int(input('Enter line No :'))
    if l_no == 0:
        break
    else:
        print(lines[l_no - 1])
