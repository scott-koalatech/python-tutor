### 13.猜数字
game_number = 42
guess_number = int(input("请输入一个数字："))
if guess_number == game_number:
    print("猜对了！")
elif guess_number > game_number:
    print("大了")
else:
    print("小了")

### 14. 统计某字符串出现的次数
string = input ("请输入一个字符串:")
char = input("请输入一个字符:")
count = string.count(char)
print("字符%s在字符串%s中出现了%d次" % (char,string,count) )

### 15. 二维列表中的最大值
list = [[3,5,1],[4,8,2],[7,6,9]]
max_value = max(list)
max_idx = list.index(max_value)
print("最大值:",max_value)
print("位置为：",max_idx)

