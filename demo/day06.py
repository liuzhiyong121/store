
shop = [
    ["Iphone 12 pro",12000],
    ["HUAWEI watch",2000],
    ["lenovo PC",5000],
    ["Mac pc",13000],
    ["卫龙辣条",5],
    ["老干妈",7.5]
]
for  index,value  in enumerate(shop):
    print(index,value)
salary = input("请输入您的薪资：")
salary = int(salary)
mycart = []
import random
z = random.randint(1,7)#1-3为lenovo的5折券；4-7为ipnone&mac的6折券
print(z)
s1=shop[2][1]
s2=shop[0][1]
while True:
    for index,value in enumerate(shop):
        print(index,"",value)
    num = input("请输入您要的商品编号：")
    if num.isdigit():
        num = int(num)
        if num > len(shop):
            print("对不起，您要的商品不存在！请选择其他商品！")
        else:
            if 1<= z <= 3:
                print("恭喜您抽中lenovo的5折券")
                shop[2][1] = shop[2][1] * 0.5
                z = z-4
            elif 4<=z<=7:
                print("恭喜您抽中ipnone&mac的6折券")
                shop[0][1] = shop[0][1] * 0.6
                z = z+4
            else:
                shop[2][1] = s1
                shop[0][1] = s2

            if salary < shop[num][1]:
                print("对不起，您的余额不足，穷鬼！")
            else:
                mycart.append(shop[num])
                salary = salary - shop[num][1]
                print("恭喜您！添加成功！您的余额为：￥",salary)
    elif num == 'q' or num == 'Q':
        print("欢迎下次光临！")
        break
    else:
        print("输入非法，别瞎弄！请重新输入！")
print("您本次的购物情况如下：")
for index,value in enumerate(mycart):
    print(index,"",value)
print("您的余额为：￥",salary)
