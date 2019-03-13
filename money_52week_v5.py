"""
"""
import math
import datetime



def save_money(money_per_week,increase_money,total_week):
    money_list=[]
    week_money_list=[]
    global saving
    saving1=6789
    for i in range(total_week):   
        # 存钱
        #sum_week=money_per_week+increase_money
        #saving+=money_per_week
        
        money_list.append(money_per_week)
        saving=math.fsum(money_list)
        saving1=math.fsum(money_list)

        # 输出
        #print("第{}周，存入{}元，累计{}元".format(i+1,money_per_week,saving))
        #print("第{}周，存入{}元，累计{}元 saving1".format(i+1,money_per_week,saving1))
        week_money_list.append(saving)
        money_per_week+=increase_money
        
    return week_money_list

def main():
    
    total_week=52
    saving=0
    saving1=5343
    i=1
    money_per_week=int(input("请输入每周存钱数目"))
    increase_money=int(input("请输入每周增加存钱数目"))
    total_week=int(input("请输入期数"))
    save_money(money_per_week,increase_money,total_week)
    week_money_list=save_money(money_per_week,increase_money,total_week)
    #saving1=save_money(money_per_week,increase_money,total_week)
    print("saving",saving)
    print("saving1",saving1)
    print("week_money_list",week_money_list)
    input_date_str=input("请输入当前的日期yyyy/mm/dd")
    datetime_input=datetime.datetime.strptime(input_date_str,"%Y/%m/%d")
    #print("多少周",datetime_input.isocalendar()[1])
    week_num=int(datetime_input.isocalendar()[1])
    print("week_money_list",week_money_list)
    print("您输入的时间是第{}周,存钱数目是{}".format(week_num,week_money_list[week_num-1]))
    
'''
 now=datetime.datetime(2017,8,5,0,0)
 
>>> now.isocalendar()
(2017, 31, 6)
>>> datatime.datetime.strftime(now,'%d/%m/%YY')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    datatime.datetime.strftime(now,'%d/%m/%YY')
NameError: name 'datatime' is not defined
>>> datetime.datetime.strftime(now,'%d/%m/%YY')
'05/08/2017Y'




    money_list=[]
    
   

        #更新下周
        money_per_week+=increase_money
        i+=1
        
    
    pass
'''
if __name__=="__main__":
    main()
