a = input("请输入一个数：")   #实现输入10个数字，并打印10个数的求和结果
b = input("请输入一个数：")
c = input("请输入一个数：")
d = input("请输入一个数：")
e = input("请输入一个数：")
f = input("请输入一个数：")
g = input("请输入一个数：")
h = input("请输入一个数：")
i = input("请输入一个数：")
j = input("请输入一个数：")
a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = int(e)
f = int(f)
g = int(g)
h = int(h)
i = int(i)
j = int(j)
print("总和为：",(a+b+c+d+e+f+g+h+i+j))
#---------------------------------------

a = input("请输入一个数：")   #依次输入十个数，打印最大值，求和，求平均值
b = input("请输入一个数：")
c = input("请输入一个数：")
d = input("请输入一个数：")
e = input("请输入一个数：")
f = input("请输入一个数：")
g = input("请输入一个数：")
h = input("请输入一个数：")
i = input("请输入一个数：")
j = input("请输入一个数：")
a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = int(e)
f = int(f)
g = int(g)
h = int(h)
i = int(i)
j = int(j)
print("总和为：",(a+b+c+d+e+f+g+h+i+j))
print("平均数为：",(a+b+c+d+e+f+g+h+i+j)/10)
if a>=b:
    s1 = a
else:
    s1 = b
if c>=d:
    s2 = c
else:
    s2 = d
if e>=f:
    s3 = e
else:
    s3 = f
if g>=h:
    s4 = g
else:
    s4 = h
if i>=j:
    s5 = i
else:
    s5 = j
if s1>=s2:
    a1 = s1
else:
    a1 = s2
if s3>=s4:
    a2 = s3
else:
    a2 = s4
if a1 >= a2:
    q1 = a1
else:
    q1 = a2
if s5>=q1:
    print("最大数为：",s5)
else:
    print("最大数为：",q1)
#---------------------------------

import random
num = random.randint(50,150)  #使用random模块产生50~150之间的数
#-----------------------------------

a = input("请输入一个数：")      #输入三边是否能够成三角形，能构成什么三角形
b = input("请输入一个数：")
c = input("请输入一个数：")
a = int(a)
b = int(b)
c = int(c)
if a+b>c and b+c>a and a+c>b and a>0 and b>0 and c>0:
    if a==b==c:
        print("等边三角形")
    elif a==b or a==c or c==b and a==b!=c or a==c!=b or b==c!=a:
        print("等边三角形")
    elif a*a + b*b == c*c or b*b + c*c == a*a or c*c + a*a == b*b:
        print("直角三角形")
    else :
        print("普通三角形")
else:
    print("不能构成三角形")
#-------------------------------------------

A = 56         #利用+实现两个数字的调换
B = 78
A = A+B
B = A - B
A = A - B
print("A=",A)
print("B=",B)
#--------------------------------------

cc = 0                       #密码账户输入三次错误锁定
while cc<3:
    cc = cc +1
    name = input("输入账号：")
    password = input ("输入密码：")
    if name != "root" or password != "admin":
        print("再次输入")
    else:
        print("输入正确")
        break
if cc==3:
    print("密码输入错误三次，系统锁定")
#-----------------------------------------------

s = 1              #利用while实现1-100的和
s1 = 0
while s<=100:
    if s<=100:
        a = a+s
        s = s+1
else:
    a = int (a)
    print(a)
#------------------------------------------

d = 0           #青蛙在20米深的井中，白天上爬3m，夜晚下降2m  ，多久能爬出井
p = 0
while p <=20:
    d = d+1
    d = int(d)
    p = p+3
    if p<=20:
        p = p-2
    else:
        print(d)
#---------------------------------------------------

import random       # 1.添加计数打印功能2.添加次数金币功能和7次锁定系统功能【退出】。
num = random.randint(1,100)
count = int(input("请输入金币数量："))
gg = 0
while count >= 50 and gg<7:
    count = count - 50
    gg = gg + 1
    a = input("请输入您要猜的数字：")
    a = int(a)
    if a > num:
        print("大了！")
    elif a<num:
        print("小了！")
    else:
        print("恭喜您，猜中了！","猜的次数为：",gg)
        gg<=3
        count = count+200
        count = int(count)
        print("恭喜您，奖励您200金币,您现在金币剩余：",count)
        break
if count < 50:
    print("您的金币余额不足够进行下一次猜数了,请充值！")
if gg >= 7:
    print("您猜数字的次数用完了！")