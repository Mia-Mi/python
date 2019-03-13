"""
"""
import math



def save_money(money_per_week,increase_money,total_week):
    money_list=[]
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
        print("第{}周，存入{}元，累计{}元".format(i+1,money_per_week,saving))
        print("第{}周，存入{}元，累计{}元 saving1".format(i+1,money_per_week,saving1))
        money_per_week+=increase_money
    return saving

def main():
    
    total_week=52
    saving=0
    saving1=5343
    i=1
    money_per_week=int(input("请输入每周存钱数目"))
    increase_money=int(input("请输入每周增加存钱数目"))
    total_week=int(input("请输入期数"))
    save_money(money_per_week,increase_money,total_week)
    saving=save_money(money_per_week,increase_money,total_week)
    #saving1=save_money(money_per_week,increase_money,total_week)
    print("saving",saving)
    print("saving1",saving1)
'''
    money_list=[]
    
   

        #更新下周
        money_per_week+=increase_money
        i+=1
        
    
    pass
'''
if __name__=="__main__":
    main()
