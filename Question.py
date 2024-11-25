### 1.计算平方和
def Sum(n):
    sum = 0
    for i in range(1,n+1):
        sum += i*i
    return sum
n = int(input("请输入："))
print(Sum(n))

### 2.列表的反转
a = [1,2,3,4,5]
a.reverse()
print('列表反转结果是: ',a)

### 3.寻找最大值
def max_num(list):
    return max(list)
list = [4,7,1,9,3]
print(max_num(list))


### 7.计算平均值
def calculate_scores(scores):   
    max_socre = max(scores)
    min_score = min(scores)
    average_score = round(sum(scores)/len(scores),2)
    return {"最高分":max_socre,  "最低分":min_score, "平均分": average_score }
scores=[85, 90, 78, 92, 88]
print(calculate_scores(scores))

### 13.猜数字


