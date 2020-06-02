#the self simply is an instance to the class
#has to be the 1st element in any function but any name

class myclass:
    def __init__(me,a,b):
        me.name=a
        me.age=b

    def myfnx(self):
        print("hi, " + self.name)

p=myclass("irene",19)
p.myfnx()