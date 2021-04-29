def lol(a,b,c):
    temp=a
    a=a-75
    for i in range((temp-75)//90):
        a=a-90
        b+=3
        c+=19
    if a>=30:
        for i in range(a//30):
            a=a-30
            b+=1
            c+=6
    for i in range(b//2):
        c-=1
    return (a,b,c)
time=input("輸入遊戲時間").split(":")
second=int(time[0])*60+int(time[1])
wave=0
army=0
result=lol(second,wave,army)
print(result[2],"隻兵")


