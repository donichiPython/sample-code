import MeCab
print(MeCab.Tagger().parse("そろそろPythonの学習に飽きてきた"))
print(MeCab.Tagger().parse("そろそろPythonの学習に飽きてきた").splitlines()[:-1])
for chunk in MeCab.Tagger().parse("そろそろPythonの学習に飽きてきた").splitlines()[:-1]:
    (surface, feature) = chunk.split('\t')
    print("surface:"+surface)
    print("feature:"+feature)
