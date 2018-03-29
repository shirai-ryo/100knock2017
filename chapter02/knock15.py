f = open('hightemp.txt')
N = int(input())

lines = f.readlines()
length = len(lines)

f.close()


f = open('hightemp.txt')
count = 0
for line in f:
    if count < length - N:
        count += 1
    else:
        print(line)
f.close()
