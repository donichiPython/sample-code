import re
print('matchメソッド。Noneはマッチしていない。<_sre.SRE_Match object;・・>はマッチした場合')
print(re.match('@|＠', 'ああああ'))
print(re.match('@|＠', 'ああ＠あ'))
print(re.match('@|＠', '＠あああ'))
print(re.match('@|＠', '＠'))

print('searchメソッド。Noneは出現していない。<_sre.SRE_Match object;・・>は出現した場合')
print(re.search('@|＠', 'ああああ'))
print(re.search('@|＠', 'ああ＠あ'))
print(re.search('@|＠', '＠あああ'))
print(re.search('@|＠',  '＠'))

print('subメソッド。@もしくは＠を削除している')
print(re.sub('@|＠', '', 'ああ＠あ'))
print(re.sub('@|＠', '', '＠あああ'))

print('subメソッド。^で先頭の@もしくは＠のみ削除している')
print(re.sub('^@|^＠', '', 'ああ＠あ'))
print(re.sub('^@|^＠', '', '＠あああ'))
