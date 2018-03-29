from knock20 import wiki_UK
import re

#print(wiki_UK())で確認すると、カテゴリを含む文には"Category:"がついている

for line in wiki_UK().split('\n'):
    obj = re.search(r'\[\[Category:.*', line)
    # 「.*」は「.」が任意の一文字、「*」は0回以上の繰り返しなので
    # Category:のあとに何もついてなくても、なんでもいいから何かついてても、サーチできる
    #MatchObject = re.search(正規表現, 検索対象の文字列)
    if obj is not None:
        print(obj)

# for line in wiki_UK().split('\n'):
#     #split()だと空白ごとで区切ってしまうので、改行コードで区切ること
#     if "Category:" in line:
#         print(line)
