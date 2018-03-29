def nekoneko():
    with open("neko.txt.mecab", "r") as text:
        n_list = [] #単語ごとのやつを一文突っ込む。一文が終われば初期化する
        k_list = [] #一文が終わった時点で突っ込む。これがメインになる
        for line in text:
            words = line.strip("\n").replace("\t", ",").split(",")
            if line.startswith('EOS'):
                if len(n_list) > 0:
                    k_list.append(n_list)
                n_list = []
            else:
                n_list.append({"surface" : words[0], "pos" : words[1], "pos1" : words[2], "base" : words[7]})
    return k_list


if __name__ == "__main__":
    print(nekoneko())

#yieldを使うとメモリ的にいいらしい。
#詳しくはググる
