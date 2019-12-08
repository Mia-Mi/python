import math
count=1
total=0
total1=0
s1=-1
s2=1
while count <= 100 :
    #total = total + count
    if (count %2) !=0 :
        #print(count)
        #print(count%4)
        if count % 4 !=3:
            total = total + count
        else:
            total = total - count
    # else:
    #     #     total = total - count
    #total=count+power(s1,count)
    count=count+1


    ##
    #fuhao=-fuhao
    # localsum=i*fuhao
    #total=total+localsum
    ###

print(total)
#print(total1)
