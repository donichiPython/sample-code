class Hello:
    def hello1(self):
         print("おはよう")
    def _hello2(self):
        print("こんにちは")
    def __hello3(self):
        print("こんばんは")

hello = Hello()
hello.hello1()
hello.hello2()
hello.hello3()
# hello._hello2()
# hello._Hello__hello3()
