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