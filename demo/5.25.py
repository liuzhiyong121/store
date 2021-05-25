
id1=1
name1="T恤"
price1=30
amount1=100
size1="s-xxxl"
add1="浙江"

id2=2
name2="牛仔裤"
price2=30
amount2=100
size2="s-xxxl"
add2="浙江"

id3=3
name3="卫衣"
price3=80
amount3=50
size3="s-xxxl"
add3="浙江"

id4=4
name4="短裤"
price4=60
amount4=180
size4="s-xxxl"
add4="浙江"

id5=5
name5="裙子"
price5=200
amount5=150
size5="s-xxxl"
add5="浙江"

id6=6
name6="帽子"
price6=20
amount6=40
size6="s-xl"
add6="浙江"

print("=========欢迎来到刘志勇的服装商城系统==========")
print("编号   名称    价格    数量     尺码      产地")
print("-----------------------------------------")
print(id1,"   ",name1,"   ",price1,"   ",amount1,"   ",size1,"  ",add1)
print(id2,"  ",name2,"   ",price2,"  ",amount2,"   ",size2,"  ",add2)
print(id3,"   ",name3,"   ",price3,"   ",amount3,"   ",size3,"  ",add3)
print(id4,"   ",name4,"    ",price4,"  ",amount4,"   ",size4,"  ",add4)
print(id5,"   ",name5,"    ",price5,"   ",amount5,"   ",size5,"  ",add5)
print(id6,"   ",name6,"    ",price6,"  ",amount6,"      ",size6,"  ",add6)
print("------------------------------------------")
print(" 总金额：￥",(price1*amount1+price2*amount2+price3*amount3+price4*amount4+price5*amount5 +price6*amount6))