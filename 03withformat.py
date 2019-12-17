# name=input(">>")
# address=input(">>")
# hobby=input(">>")
# name1=input(">>")
# address1=input(">>")
# hobby1=input(">>")
# #s="我叫%s，我喜欢在%s%s 我叫%s，我喜欢在%s%s" %(name,address,hobby) %(name1,address1,hobby1)
# s1="我叫%s，我喜欢在%s%s 我叫%s，我喜欢在%s%s" %(name,address,hobby,name1,address1,hobby1)
# s2=f"我叫{name},我喜欢在{address}{hobby}"
# print(s1)
# print(s2)

# string1=input("")
# if "马化腾" in string1:
#     string2=string1.replace("马化腾","xxx")
#     print("you")
# print(string2)
# str = "this is string example....wow!!! this is really string";
# print(str.replace("is", "was"))
# print(str.replace("is", "was", 3))
# name="alex"
# password="123456"
# name_input=str(input("name>>"))
# password_input=str(input("password>>"))
# if name_input==name and password_input==password:
#     print("ok")

# str_name=input(">>xingming")
# if str_name.startswith("张") or str_name.startswith("程"):
#     print("500")
# elif str_name.startswith("王") or str_name.startswith("李"):
#     print("300")
# else:
#     print("200")

# name="alex"
# password="123456"
# verfy_code="aX3D"
# name_input=str(input("name>>")).strip()
# password_input=str(input("password>>")).strip()
# verfy_code_input=str(input("verfy_code>>")).strip()
# if name_input==name and password_input==password and verfy_code_input.upper()=="AX3D" :
#     print("ok")

# s_input=input(">>")
# print((s_input.replace("马化腾","***").replace(" ","")))



# i=0
# s="asadasfdsfdsfsdfsdfsdfdsf"
# while  i< len(s):
#     print(s[i],end='')
#     i=i+1
# print("  ")
# for c in s:
#    #
#     print(c,end='')
#
#
# s=[1,2,3,4,5,6,7,8,9,0]
# print("_".join(str(s)))
# s1={"1","2","3","4","5","6","7","8","9","0"}
# print("_".join(s1))
# s2=(1,2,3,4,5)
# print("_".join(s2))

# lst=["23423_sb","123213_sb","2132_sb"]
# for i in lst:
#     #print(lst[item])
#     print(item)
# for i in range(len(lst)):
#     print(i,lst[i])
#     lst[i]=lst[i].replace("_sb","")
# print(
# lst)

# dic={"赵本山":"劝说小丑","范围":"道士下山","郭德纲":"相声"}
# for item in dic:
#     print("one",item,dic[item])
#
# #a,b=1,2
# for item in dic.keys():
#     print("two",item,dic[item])
# for item in dic.values():
#
#     print("three",item)
#
# for k,v in dic.items():
#     print("four",k,v)

# list_to_delete=["张1","张2","张3","张4","张5","张6","alex","mary"]
# item2_list=[]
# for itm1 in list_to_delete:
#     if itm1.startswith("张"):
#         #list_to_delete.remove(itm1)
#         item2_list.append(itm1)
# print(list_to_delete)
#
# for item3 in item2_list:
#
#     print(list_to_delete.remove(item3))
# print(list_to_delete)

cars = ['鲁A32444', '鲁B12333', '京B8989M', '黑C49678', '黑C46555', '沪B25041', '黑C34567']
locations = {'沪': '上海', '京': '北京', '黑': '黑龙江', '鲁': '⼭东', '鄂': '湖北', '湘': '湖南'}
all_cars=""
cars_short=""
cars_in_prov=""
for item in cars:
    print(item,end=" ")
    all_cars=all_cars+item
    cars_short =cars_short+item[0]
print(all_cars,end=" ")
print(cars_short,end=" ")
result={}

for item in cars_short:
    print(locations[item],end=" ")
    cars_in_prov=cars_in_prov+locations[item]
#     for x,y in locations.values()
#         if item=x:
#
    #print(cars_in_prov,end=" ")
    if result.get(locations[item]):
        result[locations[item]]+=1
    else:
        result[locations[item]]=1
print("----\n",cars_in_prov,end=" ")
print(result)


