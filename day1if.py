# a=input("dsf")
# b=input("dsfds")
# if a>b:
#     print("a 比b 大")
# elif a==b:
#     print("a 比b same")
# else:
#     print("a 比b xiao")
try:
    a=int(input("please input youre score"))
    if a>100:
        print("bukeneng")
    elif a>90:
        print("优秀")
    elif a>80:
        print("良好")
    elif a>70:
        print("zhongdeng")
    elif a>60:
        print("及格")
    elif a>0:
        print("bujige")
    else:
        print("出错！")
except OSError as err:
    print("1OS error: {0}".format(err))
except ValueError:
    print("2Could not convert data to an integer.")
except:
    print("3Unexpected error:", sys.exc_info()[0])
    raise
