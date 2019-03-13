#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
 
# 定义函数
def printme ( str ):
   print("asdsd")
   print ( str)
   return
 
# 调用函数


if __name__=="__main__":

     print ("I'm the second.")
printme("我要调用用户自定义函数!")
printme("再次调用同一函数")


if __name__=="__main1__":
    print ("I'm the 3second.")
    printme("我要ssss调用用户自定义函数!")
    printme("再次ssss调用同一函数")



def bmrcal():
    
    while (input("是否推出,y or n"))!='y':
        print("请输入如下信息，用空格分隔")

        input_string=input('sex 体重 身高 年龄')
        input_string.find(' ')
        list=input_string.split()
        print(list)
        print(type(list))
        try:
            if ((len(list)<4) or list[1].isdigit()!=True or list[2].isdigit()!=True  or list[3].isdigit()!=True) :
                print("第1个输入男 或 女，其它3个输入数字")
                sys.exit()
            else:
                
                gender=list[0]
                
                weight=float(list[1])
                height=float(list[2])
                print(type(weight),weight)
                print(type(height),height)
                if gender=='男':
                    bmr=(13.7*weight)+(5.0*height) +66
                elif gender=='女':
                    bmr=(9.6*weight)+(18*height) +655
                else:
                    bmr=-1
                if bmr !=-1:
                    print('基础代谢率:{}大卡'.format(bmr),"您的具体信息是,{},{},{},{}".format(list[0],list[1],list[2],list[3]))
                    #(list[0]),format(list[1]),format(list[2]),format(list[3])
                else:
                         print("not supported!")
        except ValueError:
            print("请输入正确的信息")
        except IndexError:
            print("输入的元素太少")
        
        except:
            print("遇到其它错误")
          

bmrcal()
#if __name__=="__bmrcal__":



#def xujiaoxing();



