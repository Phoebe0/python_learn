# 定义字典
dict1 = {"小妹": 18, "老歌": 23}
# 定义空字典
dict2 = dict()
dict3 = {}
print(dict1,dict2,dict3)

# 通过key获取value
dict4 = {"小妹": 18, "老歌": 23}
print(dict4["小妹"])

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