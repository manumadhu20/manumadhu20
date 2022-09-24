num=[4,2,1,3]
total=0
for i in range(len(num)):
    if(i%2)!=0:
        print(num[i])
        total=total+num[i]
        print("sum of numbers",total)