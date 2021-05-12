class Calc:
    def sum(self,a,b):
        result=a+b
        str="{0:f} + {1:f} = {2:f}".format(a,b,result)
        print(str)
    def sub(self,a,b):
        result=a-b
        str="{0:f} - {1:f} = {2:f}".format(a,b,result)
        print(str)
    def multi(self,a,b):
        result=a*b
        str="{0:f} * {1:f} = {2:f}".format(a,b,result)
        print(str)
    def div(self,a,b):
        result=a/b
        str="{0:f} / {1:f} = {2:.3f}".format(a,b,result)
        print(str)
    
        