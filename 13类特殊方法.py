# 面向对象第2节
##知识点：
# 多继承
# 特殊方法
# 装饰器

# 多继承
# 封装，继承，多态

class A:  # object
    def show(self):
        print('AAAA')
        print('xxxxxx')

class B:
    def fun(self):
        print ('BBBB')

class C(A,B):
    def show(self):
##        A.show(self)
        super().show()
        print('cccc')

c = C()

# 如果要完全使用自己的函数，不用使用函数调用以及super
# 想要在继承的继承上，把功能增加

# 特殊方法
#实例调用：
'''
__init__    初始化
__repr__    c1
__str__     print (c1 )(如果类里面先定义了__repr__的话print x时也会返回对应的
__call__    c1()   使实例可被调用
'''
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def __str__(self):
        return 'hahhahah'
    def __repr__(self):
        return '宽为%s,高为%s' %(self.width,self.height)
    def __call__(self):
        return 'xixixixiix'


c1 = Rectangle(3,4)

##print(c1)     # 等于c1.__str__()
##c1                #等于c1.__repr__()
##c1()            #c1.__call__ ()


























