# 题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
#
# 程序分析：用情况语句比较好，如果第一个字母一样，则判断用情况语句或if语句判断第二个字母。。

def week():
    week = input("pls enter the letter:")
    if week.upper() == "M" :
        print("Monday")
    if  "T" in week.upper():
        if "U" in week.upper():
            print("Thursday")