"""
"""
import math
from datetime import datetime

'''
def whichday():
'''
    



def main():
    input_strinput_date=input("请输入当前的日期yyyy/mm/dd")
    input_date=datetime.strptime(input_strinput_date,"%Y/%m/%d")
    print(input_date)
    year=input_date.year
    month=input_date.month
    day=input_date.day
    days_in_month_tup=(31,28,31,30,31,30,31,31,30,31,30,31)
    days=sum(days_in_month_tup[:month-1])+day
    if (year%400==0) or ((year%4==0)and (year %100!=0)):
        if month>2:
            days+=1
    print("这个是第{}天".format(days))
  
if __name__=="__main__":
    main()
