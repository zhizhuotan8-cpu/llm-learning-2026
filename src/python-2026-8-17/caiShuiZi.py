import  random

result = random.randrange(0, 100)

print("猜数游戏")

while True :
    t = int(input("请输入一个整数：\t"))
    if(t == result):
        print("恭喜你，猜对啦！！！")
        break
    elif t < result :
        print("太小了哦，还要大一点点")
        continue
    else:
        print("数太大了，要小一点点")