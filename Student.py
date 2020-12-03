
class Student:
    def __init__(self,name = None,eng = None,math = None,python = None,*args,**kwargs):
        self.name = name
        self.scores = {'eng':eng,'math':math,'python':python}
        # self.scores = {'eng':args[0],'math':args[1],'python':args[2]}
        #self.name 與 self.scores 自動裝箱到 self.__dict__(內建的元件)
        if len(args) > 0:#表示資料在args裡
            self.scores = {'eng':args[0],'math':args[1],'python':args[2]}
        elif len(kwargs) > 0:#表示資料在kwargs裡
            self.scores = kwargs
    def show(self):
        print(self.__dict__)