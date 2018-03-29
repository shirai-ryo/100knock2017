f = open('hightemp.txt')

lines = []

for i in f:
    i = i.split()
    lines.append(i)
sorted(lines, key=lambda temp: float(temp[2]))
#list.sort()はリストしかできないけど
#sorted()はそれ以外もできる
lines.reverse()

for l in lines:
    print(l)

f.close()

#sort -k 3 -n hightemp.txt
#-n　をつけないと、文字コードでソートされる
#（例えば、200度が30度より前に出てきてしまう）
