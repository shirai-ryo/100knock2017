f = open('hightemp.txt', 'r')
N = int(input())
count = 0

for line in f:
    if count % N == 0:
        print()
        #　N行を出力？したところで、空白の行を入れる
    print(line)
    count += 1

f.close()
