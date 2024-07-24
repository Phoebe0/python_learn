# Python(一) - 初识

# pyCharm使用

官网下载社区版，免费

## 快捷键
<img width="657" alt="image" src="https://github.com/user-attachments/assets/1f40573f-f70a-4bc3-8c94-93c6d9094002">


# 字面量

代码中被写下来的固定的值


```python
# 字面量
# 整数
print(10)
# 浮点数
print(13.14)
# 字符串
print("Tricia")
```

# 注释

## 单行注释

以# 开头

# 注释

## 多行注释

“”“

注释内容

“”“

```python
# 单行注释: 解释某个片段
"""
多行注释：
    1. 对文件进行解释（放到最上面） 
    2. 类注释 
    3. 方法注释
"""
```

# 变量

格式：`变量名称 = 变量值`

```python
name = "Tricia"
age = 18
print("姓名：", name)
print("年龄：", age)
age += 1
print("过了生日，年龄", age)
```

# 数据类型

Number（数字）

String（字符串）

List（列表）

Tuple（元组）

Set（集合）

Dictionary（字典）

其中，Number、String、Tuple是可变的；List、Set、Dictionary是不可变的。可变还是不可变是相对于内存地址来说的

## Number（数字）

支持 int（整型）、float（浮点型）、bool（布尔型）、complex（复数）

---

# —  — — — — 数据容器— — — — —

## String（字符串）

<aside>
💡 注意：字符串之间的比较是依据[ASCII](https://tool.oschina.net/commons?type=4)值，并且是按位比较，一位一位比。

</aside>

字符串**不支持修改**

### 索引

从前向后 0开始，从后向前 -1 开始

### 操作

```python
str = 'a b cdefgg'
# index
print(str.index("d"))  # 5

# replace  字符串替换
# 语法：字符串.replace(字符串1, 字符串2)   这个并没有修改字符串本身，而是得到了新的字符串。
new_str = str.replace('a', 'v')
print(new_str)

# split 字符串分割，存入列表
list1 = str.split(' ')
print(list1)

# strip  去除前后空格
str2 = ' adbg '
print(str2.strip())
# strip  去除前后指定字符串
str3 = '11aaa'
print(str3.strip('11'))
# 统计字符串中某字符串出现的次数  count()
str4 = 'aaaaab'
print(str4.count('a'))

# 统计字符串长度 len()
print(len(str4))
```

### 遍历字符串

while循环

for循环

## List（列表）

### 语法

定义空列表

```python
变量名称= []
变量名称 = list()
```

### 概念

1. 列表可以一次性存储多个数据
2. 存储的数据类型不作限制

### 索引

从前向后 0开始，从后向前 -1 开始

```python
# list类型
name_list = ['TT', 'Vv']
print(name_list)
print(type(name_list))

# 列表可以存储不同类型的数据
my_list = [1, 'Rr', [0, 1], True]
print(my_list)

# 定义嵌套列表
two_list = [[0, 1, 2, 3], [4, 5]]
print(two_list)

# 列表索引
list_1 = [1, 2, 3, 4]
# 取数字 1
print(list_1[0])
print(list_1[-4])

# 嵌套列表取数字
list_2 = [[0, 1, 2, 3], [4, 5]]
# 取出5
print(list_2[1][1])
```


### 列表操作

1. 查询某元素
    
    ```python
    # 语法：列表.index(元素)。查询不到时，报错ValueError
    
    list_1 = [1, 2, 3, 4]
    print(list_1.index(3))  # out: 2
    ```
    
2. 修改某元素
    
    ```python
    # 语法：列表[下标] = 值
    # 修改
    list_2 = [1, 2, 3, 4, 0]
    list_2[-1] = 5
    print(list_2) # [1,2,3,4,5]
    ```
    
3. 插入元素
    
    ```python
    # 语法：列表.insert(zh下标, 元素) 
    list_3 = [1, 2, 3]
    list_3.insert(1, 0)
    print(list_3)  # [1, 0, 2, 3]
    ```
    
4. 追加元素：
    1. 单个元素插入到列表尾部
        
        ```python
        # 语法：列表.append(元素)
        list_4 = [0, 1, 2, 3]
        list_4.append(4)
        print(list_4)  # [0, 1, 2, 3, 4]
        ```
        
    2. 一批元素追加到列表尾部
        
        ```python
        # 语法：列表.extend(其他容器)
        list_4 = [0, 1, 2, 3]
        list_4.extend([5, 6, 7])
        print(list_4) # [0, 1, 2, 3, 4, 5, 6, 7]
        ```
        
5. 删除元素
    
    ```python
    # 语法1: del列表[下标]
    # 删除元素
    list_5 = [8, 9, 10, 11]
    del list_5[0]
    print(list_5)  # [9, 10, 11]
    
    # 语法2: 列表.pop(下标)
    list_5.pop(0)
    print(list_5) # [10, 11]
    
    # 删除某元素在列表中**第一个**匹配项。 语法：列表.remove(元素)
    list_5 = [8, 9, 10, 11, 8]
    list_5.remove(8)  
    print(list_5)  # [9, 10, 11, 8]
    
    ```
    
6. 清空列表

```python
#语法：列表.clear()
list_5 = [8, 9, 10, 11]
list_5.clear() # []
```

1. 统计元素数量
    
    ```python
    # 语法：列表.count(元素)
    list_6 = [1, 2, 1, 2, 3]
    num = list_6.count(1)
    print(num)  # 2
    ```
    
2. 统计全部元素数量
    
    ```python
    list_6 = [1, 2, 1, 2, 3]
    total_num = len(list_6)
    print(total_num)  # 5
    ```
    

### 遍历列表

1. for循环遍历
    
    ```python
    list_1 = [0, 1, 2, 3]
    # 定义一个循环遍历函数 - for循环
    
    def ls_for_fn(ls):
        for i in ls:
            res = ls[i]
            i += 1
            print(res)
    
    ls_for_fn(list_1)
    ```
    
2. while循环遍历
    
    ```python
    list_1 = [0, 1, 2, 3]
    # 定义一个循环遍历函数 - while循环
    
    def ls_while_fn(ls):
        n = 0
        while n < len(ls):
            res = ls[n]
            n += 1
            print(res)
    
    ls_while_fn(list_1)
    ```
    

## Tuple（元组）

### 语法

```python
# 定义元组字面量
(元素,元素,...,元素)
# 定义元组变量
变量名称 = (元素,元素,...,元素)
# 定义空元素
变量名称 = ()
变量名称 = tuple()
```

元组同列表一样，也是可以封装多个，不同的数据类型在内的容器

与列表不同的是，**元组不可修改。**

```python
# 定义元组
t1 = (1, 'tt', True)
t2 = ()
t3 = tuple()

# 定义单个元素元组
# 如果要定义单个元素的元组，后面要加一个 逗号
t4 = ('Tt', )

# 定义嵌套元组
t5 = ((0, 1, 2), (3, 4))

# 根据下标取出元组
res = t5[1][0]  # 3
print(res)
```

### 操作

```python
# index() 查找某个数据，如果数据存在则返回对应下标，否则报错
t1 = (0, 1, 1, 2)
print(t1.index(1))  # 1
# print(t1.index(3))  # 报错

# count() 统计某个数据在当前元组出现的次数
print(t1.count(1))  # 2
# len(元组) 统计元组内的元素个数
print(len(t1))  # 4
```

### 遍历元组

```python
# while 遍历 元组
t = (0, 1, 2, 3, 3)
index = 0
while index < len(t):
    print(t[index])
    index += 1
# for循环遍历 元组
for i in t:
    print(t[i])
```

### 注意

虽然元组不可修改，但是元组中的list可以修改

```python
t2 = (0, 11, ['Tt', 'Oo'])
t2[2][0] = 'Xx'
print(t2)
```


## 序列

列表，元组，字符串都是序列

### 操作 - 切片

语法：`序列[起始下标:结束下标:步长]`

表示从序列中，指定位置开始，依次取出元素，到指定位置结束得到一个**新序列**。

结束下标（不包含）

**步长：**

- 依次取元素的间隔
- 步长为n表示每次跳过n - 1个元素取
- 步长为负数，反向取【这时候起始下标和结束下标也要反向标】

```python
# 列表切片
list1 = [0, 1, 2, 3]
new_list1 = list1[0:2:1]
print(new_list1)

# 元组切片
t1 = (0, 1, 2, 3, 4, 5)
new_t1 = t1[0:4:2]
print(new_t1)

# 对字符串切片  步长为负
str1 = 'Hello World'
# 从下标8开始到下表为0结束
new_str1 = str1[8:0:-1]
print(new_str1)
# 从头到尾倒序步长为-2
new_str2 = str1[::-2]
print(new_str2)
```

## Set（集合）

### 概念

不支持元素的重复，且无序。

因为是无序，所以不支持下标索引

### 语法

```python
# 定义集合字面量
{元素1,元素2,...}
# 定义元素变量
变量名 = {元素1,元素2,...}
# 定义空集合
变量名 = set()

```

### 操作 - 修改

```python
# 集合添加元素
my_set = {0, 1, 2, 3}
my_set.add(9)
print(my_set)

# 集合删除元素
my_set.remove(0)
print(my_set)

# 清空集合
set1 = {0, 1, 2}
set1.clear()
print(set1)

# 取两个集合的差集
set2 = {0, 1, 2, 3}
set3 = {1, 4, 5, 6}
set4 = set2.difference(set3)
print(set4)

# 消除两个集合的差集 - 在集合1内部删除集合2相关的元素 - 集合1被修改，集合2不变
set2.difference_update(set3)
print(set2, set3)

# 两个集合合并成一个
set4 = {0, 1, 2}
set5 = {1, 3, 4, 5}
set6 = set4.union(set5)
print(set6)

# 统计集合元素数量
num = len(set6)
print(num)

# 集合不支持下标索引，不支持while循环遍历，可用for遍历
set7 = {0, 1, 23}
for k in set7:
    print(k)
```

## Dictionary（字典）

### 概念

通过字典，可以实现 通过key取出value操作。

字典中的key不能重复。

字典中的key 和value可以是**任意数据类型【key不能是字典】**

### 语法

```python
# 定义字典字面量
{key:value,key:value...}
# 定义字典变量
dict1 = {key:value,key:value...}
# 定义空字典
dict1 = {}
dict1 = dict()

```

### 嵌套字典

如下图，转为字典格式

```python

# 定义嵌套字典
prn_score_dict = {
    "王力宏": {
        "语文": 77,
        "数学": 66,
        "英语": 33,
    },
    "周杰伦": {
            "语文": 88,
            "数学": 86,
            "英语": 55,
        },
    "林俊杰": {
            "语文": 99,
            "数学": 96,
            "英语": 66,
        },
}
print(prn_score_dict)
# 从嵌套字典中获取数据
score = prn_score_dict["周杰伦"]["数学"]
print(f"周杰伦数学成绩：{score}")
```

### 操作

```python
# 新增元素
# 语法：字典[key] = value , 结果：字典被修改，新增了元素
dict1 = {
    "大明": 99,
    "丽丽": 45
}

dict1["阿米"] = 78
print(dict1)

# 更新元素
# 语法：字典[key] = value ，对已存在的key进行操作，元素就会被更新
dict1["大明"] = 10
print(dict1)

# 删除元素
# 语法：字典.pop(key)
dict1.pop("丽丽")
print(dict1)

# 清空元素
# 语法：字典.clear()
dict1.clear()
print(dict1)

# 获取全部key
dict2 = {
    "小富": 92,
    "胖湖": 35
}
keys = dict2.keys()
print(keys)
# 遍历字典
# 通过获取到的全部key遍历
for k in keys:
    print(f"字典的key是：{k}")
    print(f"字典的value是：{dict2[k]}")
# 直接对字典进行for循环，每一次循环都是直接得到key
for k in dict2:
    print(f"字典的key是{k}")
    print(f"字典的value是：{dict2[k]}")

# 统计字典元素数量
num = len(dict2)
print(num)
```

# — — — — — — — — — — — —

# 数据容器概念

## 数据容器之间的转换

1.  `list(容器)` - 将给定容器转换为列表
2. `str(容器)` - 将给定容器转换为字符串
3. `tuple(容器)` - 将给定容器转换为元组
4. `set(容器)` - 将给定容器转换为集合

## 数据容器排序

`sorted(容器,[reverse = True])` reverse 表示排序结果是否进行反转

排序的结果是会都变成列表对象

```python
my_list1 = [0, 6, 3, 4, 1, 2, 5]
my_tuple1 = (0, 6, 3, 4, 1, 2, 5)
print(sorted(my_list1))
print(sorted(my_tuple1, reverse= True))
```

## 验证数据类型

### type

`type(要验证的数据)`

```python
# 数据类型
# 使用print直接输出类型
print(type(10))
# 使用变量存储type()的结果
ty = type("执行")
print(ty)
# 使用type()查看变量中存储的数据类型
# 注意：变量没有类型，数据有类型
money = 10000.89
print(type(money))
```


### isinstance

## 数据类型转换

转换语句：这些语句是带有返回值的，可以直接输出

| 函数 | 说明 |
| --- | --- |
| int(x) | 转换为整型 |
| float(x) | 转换为浮点型 |
| str(x) | 转换为字符串 |

```python
# 数据类型转换
num_str = str(10)
print(num_str, type(num_str))
str_num = int("22")
print(str_num, type(str_num))
float_num = int(13.14)
print(float_num, type(float_num))
str_float = float("77.8888")
print(str_float, type(str_float))
```


# 标识符

1. 包含：英文、中文、数字、下划线（不能数字开头）
2. 不可使用关键字
   
    
3. **大小写敏感**

## 命名规范

1. 见名知意
2. 下划线命名
3. 英文字母小写

# 运算符

## 算术运算符

| 运算符 | 说明 |
| --- | --- |
| + | 加 |
| - | 减 |
| * | 乘 |
| / | 除 |
| // | 取整除 |
| % | 取余数 |
| ** | 指数 |

```python
# 加
print("加", 10 + 1)
# 减
print("减", 10 - 1)
# 乘
print("乘", 10 * 2)
# 除
print("除", 10 / 5)
# 整除
print("取整除", 10 // 3)
# 余
print("余", 10 % 2)
# 指数
print("指数", 10 ** 2)
```


## 赋值运算符

= : 将等号右边的值赋给左边

```python
name = "pp"
num = 10
num += 10
print(num)  # 20
print(name)  # pp
```

## 比较运算符

# 字符串

## 定义方式

1. 单引号
2. 双引号
3. 三引号

如果想定义的字符串包含引号，用不同的引号包裹或转义

## 拼接

通过加号。

注意：加号只能拼接字符串，不能拼接整型浮点型等等

## 字符串格式化

### 占位拼接

| 符号 | 说明 |
| --- | --- |
| %s | 转化为字符串 |
| %d | 转化为整数 |
| %f | 转化为浮点数 |


```python

# 占位拼接
# %s表示要占位的位置

name = 'Tricia'
age = 18
year = 2005
msg = '你好，%s，出生年份：%s' % (age, year)
print(msg)
```

### f”{}”进行占位

语法：`f“内容{变量}”`

```python
# f"{}"进行占位
msg1 = f'你好, {name}, 年龄{age}, 出生：{year} '
print(msg1)
```


### 格式化表达式

```python
# 格式化表达式
print("1+1的结果是%d" % (1 + 1))
print(f"10*2的结果是{10 * 2}")
```


## 精度控制

使用辅助符号m.n控制精度

m,控制宽度，要求是数字。宽度不够会用空格补齐。m比数字本身长度小时，不生效

n，控制精度，会进行四舍五入

```python
num = 23.6
print('%6.2f' % num)
```


# 数据输入

input；默认接受的类型都是字符串

- 使用input可以从键盘获取输入
- 使用变量接受输入的数据

```python
name = input("你的名字？")
print(f"你好{name}")
age = int(input("你的年龄"))
print(f"你{age}岁, 类型{type(age)}")
```
