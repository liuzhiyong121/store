print("------循环遍历出所有key-------")
dict = {"k1":"v1","k2":"v2","k3":"v3"}
keys = dict.keys()
for key in keys:
    print(key)
print("------循环遍历出所有value------")
values = dict.values()
for key in keys:
    print(dict.get(key))
print("------在字典中增加一个键值对 k4：v4--------")
dict["k4"] = "v4"
print(dict)
print("------将苹果，香蕉，葡萄加入字典---------")
info = {}
info ["苹果"]=[32.8]
info ["香蕉"]=[22]
info ["葡萄"]=[15.5]
print(info)
print("------计算money的金额---------")
Friuts = {
	'苹果':12.3,  # 水果和单价
	'草莓':4.5,
    '香蕉':6.3,
    '葡萄':5.8,
    '橘子':6.4,
    '樱桃':15.8
}
info = {
    '小明': {
        'fruits': {'苹果':4, '草莓':13, '香蕉':10},

        'money':0
    },
    '小刚': {
        'fruits': {'葡萄':19, '橘子':12, '樱桃':30},
        'money':0
    }
}
name = input("名字:")
if name in info :
    for i in info[name]['fruits'] :
        if i in Friuts :
            info[name]['money'] = info.get(name).get('money') + info.get(name).get('fruits').get(i) * Friuts.get(i)
    print(name,"的账单为",info[name]['money'])
else:
    print("非法输入")

print("------编写一个函数，传入一个列表，并统计每个数字出现的次数。返回字典数据：{21:3,56:9,10:3}------")
li = [21,21,21,56,56,56,56,56,56,56,56,56,10,10,10]
z = {}
i = 0
while i<len(li):
    count = 0
    k = 0
    flag = 0
    while k<i:
        if li[i] == li[k]:
            flag = 1
            break
        k = k + 1
    if flag == 1:
        i = i+1
        continue
    j = i
    while j < len(li):
        if li[i] == li[j]:
            count = count + 1
        j = j + 1
    s1=li[i]
    s2=count
    z[s1] = s2
    i = i + 1
print(z)

print("------将中国所有的省会城市添加到字典中-------")
citys = {
    "010":"北京"
}
citys["020"] = "上海"
citys["030"] = "广州"
citys["040"] = "济南"
citys["050"] = "石家庄"
citys["060"] = "长春"
citys["070"] = "哈尔滨"
citys["080"] = "沈阳"
citys["090"] = "呼和浩特"
citys["0100"] = "乌鲁木齐"
citys["0110"] = "兰州"
citys["0120"] = "银川"
citys["0130"] = "太原"
citys["0140"] = "西安"
citys["0150"] = "郑州"
citys["0160"] = "合肥"
citys["0170"] = "南京"
citys["0180"] = "杭州"
citys["0190"] = "福州"
citys["0200"] = "广州"
citys["0210"] = "南昌"
citys["0220"] = "海口"
citys["0230"] = "南宁"
citys["0240"] = "贵阳"
citys["0250"] = "长沙"
citys["0260"] = "武汉"
citys["0270"] = "成都"
citys["0280"] = "昆明"
citys["0290"] = "拉萨"
citys["0300"] = "西宁"
citys["0310"] = "天津"
citys["0320"] = "重庆"
citys["0330"] = "台北"
citys["0340"] = "香港"
citys["0350"] = "澳门"
print(citys)

print("------声明一个列表-------")
students = [
    {'name':'张三','age':23,'score':88,'tel':'23423532','gender':'男'},
    {'name':'李四','age':26,'score':80,'tel':'12533453','gender':'女'},
    {'name':'王五','age':15,'score':58,'tel':'56453453','gender':'男'},
    {'name':'赵六','age':16,'score':57,'tel':'86786785','gender':'3'},
    {'name':'小明','age':18,'score':98,'tel':'23434656','gender':'女'},
    {'name':'小红','age':23,'score':72,'tel':'67867868','gender':'女'},
]
print("------统计不及格人数-------")
i=0
count = 0
while i<len(students):
    if students[i].get('score')<60:
        count = count + 1
        i = i + 1
    else:
        i = i + 1
print(count)

print("------打印不及格的学生姓名，成绩-------")
i=0
while i<len(students):
    if students[i].get('score')<60:
        print("姓名：",students[i].get('name'),"\t","成绩：",students[i].get('score'))
        i = i + 1
    else:
        i = i + 1

print("------统计未成年学生个数-------")
i=0
count = 0
while i<len(students):
    if students[i].get('age')<18:
        count = count + 1
        i = i + 1
    else:
        i = i + 1
print(count)

print("------打印手机尾号是8的学生名-------")
i=0
while i<len(students):
    a = students[i].get('tel')
    a = int(a)
    while True:
        s = a % 10
        if s == 8:
            print(students[i].get('name'))
            i = i + 1
            break
        else:
            i = i + 1
            break

print("------打印最高分和对应的学生名-------")
i = 0
j = 0
while j < len(students):
        if students[i].get('score') >= students[j].get('score'):
            j = j + 1
        else:
            i = j
print("最高分数",students[i].get('score')," ","姓名",students[i].get('name'))

print("------将列表按学生成绩从大到小排序-------")
list = []
i = 0
while i<=5:
    a = students[i].get('score')
    list.append(a)
    i = i + 1
for m in range(len(list)):
    for n in range(m, len(list)):
        if list[m]< list[n]:
            s = list[n]
            list[n] = list[m]
            list[m] = s
print(list)

print("------删除性别保密的所有学生-------")
a ='保密'
b = students
for m in range(len(students)-1):
    print(m)
    s = students[m].get('gender')
    if s==a:
        b.remove(students[m])
print (b)

print("------将旅游系统与商城系统结合在一起，实现可旅游可买东西的功能-------")
shop = [
    ["Iphone 12 pro",12000],
    ["HUAWEI watch",2000],
    ["lenovo PC",5000],
    ["Mac pc",13000],
    ["卫龙辣条",5],
    ["老干妈",7.5]
]
city = {
    "北京":{
        "昌平":{
            "天通苑":["海底捞","呷哺呷哺"],
            "龙泽":{"永辉超市":[],"永旺超市":[]}
        },
        "海淀":{
            "公主坟":["军事博物馆","中华世纪园"],
            "科普场馆":["中国科技馆","北京天文馆"],
            "高校":["北京大学","清华大学"]
        },
        "朝阳":{
            "龙城":["鸟化石国家地质公园","朝阳南北塔"],
            "双塔":["朝阳凌河公园","朝阳凤凰山"]
        }
    },
    "上海":{}
}
def print_city(data):
    for i in data:
        print(i,"\t")
print_city(city)
chose1 = input("请输入城市:chose1>>>")
while True:
    if chose1 in city:
        print_city(city[chose1])
        chose2 = input("请输入二号景区chose2>>>：")
        if chose2 in city[chose1]:
            print_city(city[chose1][chose2])
            chose3 = input("请输入三号景区chose3:>>>>")
            if chose3 in city[chose1][chose2]:
                print_city(city[chose1][chose2][chose3])
                chose4 = input("请输入四号景区chose3:>>>>")
                if chose4 in city['北京']['昌平']['龙泽']:
                    for index, value in enumerate(shop):
                        print(index, value)
                    salary = input("请输入您的薪资：")
                    salary = int(salary)
                    mycart = []
                    import random
                    z = random.randint(1, 7)  # 1-3为lenovo的5折券；4-7为ipnone&mac的6折券
                    print(z)
                    s1 = shop[2][1]
                    s2 = shop[0][1]
                    f = 0
                    while True:
                        for index, value in enumerate(shop):
                            print(index, "", value)
                        num = input("请输入您要的商品编号：")
                        if num.isdigit():
                            num = int(num)
                            if num > len(shop):
                                print("对不起，您要的商品不存在！请选择其他商品！")
                            else:
                                if 1 <= z <= 3:
                                    print("恭喜您抽中lenovo的5折券")
                                    shop[2][1] = shop[2][1] * 0.5
                                    z = z - 4
                                elif 4 <= z <= 7:
                                    print("恭喜您抽中ipnone&mac的6折券")
                                    shop[0][1] = shop[0][1] * 0.6
                                    z = z + 4
                                else:
                                    shop[2][1] = s1
                                    shop[0][1] = s2

                                if salary < shop[num][1]:
                                    print("对不起，您的余额不足，穷鬼！")
                                else:
                                    j = shop[num][1] // 100
                                    f = f + j
                                    mycart.append(shop[num])
                                    salary = salary - shop[num][1]
                                    print("恭喜您！添加成功！您的余额为：￥", salary, )
                        elif num == 'q' or num == 'Q':
                            print("欢迎下次光临！")
                            break
                        else:
                            print("输入非法，别瞎弄！请重新输入！")
                    print("您本次的购物情况如下：")
                    for index, value in enumerate(mycart):
                        print(index, "", value)
                    print("您的余额为：￥", salary)
                    print("您的积分为：", f)
            elif chose3 == 'q' or chose3 == 'Q':
                print("欢迎下次光临！")
                break
