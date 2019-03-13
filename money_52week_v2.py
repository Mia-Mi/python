"""
"""
import math

def main():
    
    total_week=52
    saving=0
    i=1
    money_per_week=10
    increase_money=10
    money_list=[]
    
    while i<= total_week:   
        # 存钱
        #sum_week=money_per_week+increase_money
        #saving+=money_per_week
        money_list.append(money_per_week)
        saving=math.fsum(money_list)

        # 输出
        print("第{}周，存入{}元，累计{}元".format(i,money_per_week,saving))

        #更新下周
        money_per_week+=increase_money
        i+=1
        
    
    pass
if __name__=="__main__":
    main()
