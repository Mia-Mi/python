#
# def jiecheng(n):
#     if n > 1:
#         return n*jiecheng(n-1)
#     else:
#         return n
# print(jiecheng(5))
#
# def jiecheng1(n):
#     while n > 1:
#         return n*jiecheng(n-1)
#     else:
#         return n
# print(jiecheng1(5))
#
# def jiecheng2(n):
#     result1=1
#     for i in range (1,n+1):
#         result1=result1*i
#         #print(i)
#     return result1
# print(jiecheng2(5))
#
#
# # def add(a,b):
# #     return a+b
# # print(add(3,5))

#
# def chi(mainfood,fufood,tang,tiandian):
#     print(mainfood,fufood,tang,tiandian,sep="__")
# chi("rice","niurou","jidantang","hanggengdas")
# chi("rice","niurou",tang="jidantang",tiandian="hanggengdas")
# chi("rice","niurou",tiandian="hanggengdas",tang="jidantang")
# #chi("rice",tiandian="hanggengdas","niurou",tang="jidantang")
#chi(mainfood="rice",tiandian="hanggengdas",fufood="niurou",tang="jidantang")

# def log(name,age,gender="男"):
#     print(name,age,gender)
# log("zhangwuji",23)
# log("wusong",34)
# log("wusong",34,"男")
# log("sunerniang",60,"女")
# log("wusong",34,"safsd")

# def chi1(*food):
#     print(food)
# chi1("damifan")
# chi1("damifan","hulatang")
# chi1("hulatang","xiancai","yadan")
# chi1("damifan","damifan","damifan","hulatang","xiancai","yadan")

# def chi2(**food):
#     print(food)
# chi2(a="damifan")
# chi2(main_food="damifan",hehe="hulatang")
# chi2(haha="hulatang",haha1="xiancai",haha2="yadan")
# chi2(haha="damifan",haha2="damifan",haha3="damifan",haha4="hulatang",haha6="xiancai",haha5="yadan")
# #chi2(haha="damifan",haha=2"damifan",haha3="damifan",haha4="hulatang",haha6="xiancai",haha5="yadan")
#
# def func(a,b,c,*args,d=10,**kwargs):
#     print(a,b,c)
#     print(args)
#     print(d)
#     print(kwargs)
# #
# # fun(1,2,3,4,5,6,7,8,9,10)
# # func(1,2,3,d=20,a=3,b=5,c=6)
#


# def func3():
#     def func4():
#         print("wo shi func4")
#     return func4
# ret=func3()
# ret()
#
# def func5():
#     def func6():
#         print("wo shi func6")
#     return func6
# ret=func5()
# ret()


# def funct(fn):
#     func7()
# def func7():
#     print("func7")
# funct(func7)
# def zhuangshiqi(fn):
#     def inner():
#         login()
#         fn()
#     return inner
#
# @zhuangshiqi
# def adduser():
#     print("add user")
# def updateuser():
#     print("update user")
# def deluser():
#     print("del user")
# def login():
#     print("login")
#
# # adduser=zhuangshiqi(adduser)
# # updateuser=zhuangshiqi(updateuser)
# # deluser=zhuangshiqi(deluser)
# adduser()
# updateuser()

#
# def waigua(fn):
#     def inner(*args,**kwargs):
#         print("start waigua")
#         ret=fn(*args,**kwargs)
#         print("stop waigua")
#         return ret
#
#     return inner
# @waigua
# def play_dnf(qq,qqmima):
#     print("qq 登录")
#
#     print("paly_dnf")
#
# @waigua
# def play_wangzhe():
#     print("qq 不登录")
#
#     print("玩王者")
#     return 50000
#
# play_dnf(343243,"asdae")
# print(play_wangzhe())

# lst={"1","2","3","4","5"}
# it=lst.__iter__()
# while(1):
#     try:
#         print(it.__next__())
#     except StopIteration:
#         print("no data")
#         break
#
# lst1={"a1","a2","a3","a4","a5"}
# it1=lst1.__iter__()
# while(1):
#     try:
#         print(it1.__next__())
#     except StopIteration:
#         print("no data")
#         break
#

def fun_shengchengqi():
    print("hehe hehehe ")
    yield "hahahahha"
    print("2hehe hehehe ")
    yield "2hahahahha"

# ret1=fun_shengchengqi()
# print(ret1)
# rr=ret1.__next__()
# print(ret1)
# rr=ret1.__next__()
# print(ret1)
# # rr=ret1.__next__()
# # print(ret1)


# def fun_shengchengqi_50():
#     lst=[]
#     print("hehe hehehe ")
#     for i in {1,10000}:
#         print("")
#         lst.append(i)
#         if len(lst)==50:
#             yield "50个"
#
# ret11=fun_shengchengqi_50()
# print(ret11)
# rr=ret11.__next__()
# print(ret1)
# rr=ret11.__next__()
# print(ret11)
# # rr=ret11.__next__()
# # print(ret11)

'''推导式'''
list1=[i*i for i in range(1,21)]
print(list1)
list2=["yifu"+str(i) for i in range(1,101)]
print(list2)





















