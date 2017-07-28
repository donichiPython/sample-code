class Taiyakigata:
    def __init__(self,naka):
        self.nakami = naka
    def answer(self):
        print('このたいやきの中身は、',self.nakami)

taiyaki1 = Taiyakigata('あんこ')
taiyaki2 = Taiyakigata('カスタード')
taiyaki1.answer()
taiyaki2.answer()
