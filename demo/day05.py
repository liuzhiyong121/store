#求选课学生总共有多少人
chinese = ['小明','小张','小黄','小杨']
math =['小黄','小李','小王','小杨','小周']
english = ['小杨','小张','小吴','小冯','小周']
li = math+chinese+english

m=0
i = 0
while i < len(li):
    count = 0
    k = 0
    flag = 0
    while k < i:
        if li[i] == li[k]:
            flag = 1
            break
        k = k + 1
    if flag == 1:
        i = i + 1
        continue
    j = i
    while j < len(li):
        if li[i] == li[j]:
            count = count + 1
        j = j + 1
    print(li[i],"出现了",count,"次！")
    m = m +1
    i = i + 1
print("一共有：",m,"人选课")

#求只选了第一个学科的人的数量和对应的名字
for index,value in enumerate(chinese):
    print(value)
print("共有人数：",len(chinese))
#求只选了一门学科的学生的数量和对应的名字
i = 0
s =0
while i < len(li):
    count = 0
    k = 0
    flag = 0
    while k < i:
        if li[i] == li[k]:
            flag = 1
            break
        k = k + 1
    if flag == 1:
        i = i + 1
        continue
    j = i
    while j < len(li):
        if li[i] == li[j]:
            count = count + 1
        j = j + 1
    if count<=1:
        print(li[i])
        s =s+1
    i = i + 1
print ("只选了一门学科的人数：",s)

#求只选了语文和英语的学生的数量和对应的名字
su = chinese + english
m = 0
i = 0
while i < len(su):
    count = 0
    k = 0
    flag = 0
    while k < i:
        if su[i] == su[k]:
            flag = 1
            break
        k = k + 1
    if flag == 1:
        i = i + 1
        continue
    j = i
    while j < len(su):
        if su[i] == su[j]:
            count = count + 1
        j = j + 1
    print(su[i])
    m = m +1
    i = i + 1
print("共有人数：",m)

#编程实现
i = 9
while i>= 1:
    j = i
    while j >=1:
        print(j,"x",i,"=",(j*i)," ",end="")
        j = j-1
    print()
    i = i -1