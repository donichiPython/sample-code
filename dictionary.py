dictionary = {"ニックネーム": "ななこ", "性別": "女性", "趣味": "映画鑑賞"}
print(dictionary["趣味"])
print(len(dictionary))
dictionary["趣味"] = "音楽鑑賞"
dictionary["職業"] = "新米プログラマ"
del dictionary["性別"]
print(dictionary)
