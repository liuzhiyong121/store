q = 1
while q <= 7:
    k=7
    while k>=q:
        j = 1
        print(" ",end="")
        k=k-1
    while j<=q:
        print("* ",end="")
        j = j+1
    print()
    q = q+1





l = ["北京","上海","广东"]
l.append("济南")
l.append("石家庄")
l.append("长春")
l.append("哈尔滨")
l.append("沈阳")
l.append("呼和浩特")
l.append("乌鲁木齐")
l.append("兰州")
l.append("银川")
l.append("太原")
l.append("西安")
l.append("郑州")
l.append("合肥")
l.append("南京")
l.append("杭州")
l.append("福州")
l.append("广州")
l.append("南昌")
l.append("海口")
l.append("南宁")
l.append("贵阳")
l.append("长沙")
l.append("武汉")
l.append("成都")
l.append("昆明")
l.append("拉萨")
l.append("西宁")
l.append("天津")
l.append("重庆")
l.append("台北")
l.append("香港")
l.append("澳门")





l[1]="广东"
l[2]="上海"
print(l)

d=[36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
s=sum(d)
p = s/8
print("总和",round(s))
print("平均值",round(p))



a = [1, 5, 21, 30, 15, 9, 30, 24]
i= 0
s= 0
num =0
while i<=7:
    i=i+1
    if  a[num] % 5 == 0:
        print(a[num])
        s = s+a[num]
        num=num+1
    else:
        num = num+1
print(s)



list = [1,2,3,4,5,6,7,8,9]
list.reverse()
print(list)


import collections
a = [5,2,4,8,6,2,1,4,7,5,4,1,2,3,5,8,4,1,2]
b = collections.Counter(a)
for c in b:
    print(c,"出现",b[c],"次")








