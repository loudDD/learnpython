# 题目：按逗号分隔列表。

a = ["1","2","3","4"]
v = [1,2,3,4]

b = ",".join(a)
print(b)

c = ",".join(str(i) for i in v )

print(c)