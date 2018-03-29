from knock30 import nekoneko

for line in nekoneko():
    #一行ごと
    for i in line:
        #一行の中の、単語ごと（辞書になってる）
        print(i["surface"])
        #単語ごとのマップ型から、surfaceに当たるものを取り出す

        #ダメだったやつ
        # print(line[i]["surface"])
