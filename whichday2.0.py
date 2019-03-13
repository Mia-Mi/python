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
    days_in_month_list=[31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap_year(year)==True:
        days_in_month_list[1]=29
    days=sum(days_in_month_list[:month-1])+day
    
    #if month>2 and is_leap_year(year):
    #        days+=1
    print("这是{}年第{}天".format(year,days))
  
if __name__=="__main__":
    main()
