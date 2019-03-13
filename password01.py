"""
""" 
import math
from datetime import datetime


def is_leap_year(year):
    is_leap=False
    if (year%400==0) or ((year%4==0)and (year %100!=0)):
        return True
    else:
        return False
    return is_leap

    



def main():
    input_strinput_date=input("请输入当前的日期yyyy/mm/dd")
    input_date=datetime.strptime(input_strinput_date,"%Y/%m/%d")
    print(input_date)
    year=input_date.year
    month=input_date.month
    day=input_date.day

    #包含30的集合
    days=day
    # _30_days_month_set={4,6,9,11}
    # _31_days_month_set={1,3,5,7,8,10,12}
    month-day_dict={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    month-day_dict1={30:{4,6,9,11},31:{1,3,5,7,8,10,12}}
    for i in range(1,month):
        if i in _30_days_month_set:
            days+=30
        elif i in _31_days_month_set:
            days+=31
        else:
            days+=28

    
    #days_in_month_list=[31,28,31,30,31,30,31,31,30,31,30,31]
    #if is_leap_year(year)==True:
    #    days_in_month_list[1]=29
    #days=sum(days_in_month_list[:month-1])+day
    
    if month>2 and is_leap_year(year):
            days+=1
    print("这是{}年第{}天".format(year,days))
  
if __name__=="__main__":
    main()
