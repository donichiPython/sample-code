file = open('read.txt', 'r', encoding='Shift_JIS')
text = file.read()
print(text)
file.close()