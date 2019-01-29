# def LetterChanges(str):
#     letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW"
#     changes = "bcdEfghIjklmnOpqrstUvwxyzABCDEFGHIJKLMNOPQRSTUVWZ"
#     mapping = {k: v for (k, v) in zip(str + letters, str + changes)}
#     print(str+letters)
#     print(str+changes)
#     print(letters+changes)
#     print( "".join([mapping[c] for c in str]))
#
# LetterChanges("asX")
#


# keep this function call here
# print(LetterChanges(input()))

# m = [[1, 2, 3],  [4, 5, 6],  [7, 8, 9]]
# n = [[2, 2, 2],  [3, 3, 3],  [4, 4, 4]]
# print(a*b for a,b in zip(m,n))
# print([x*y for a, b in zip(m, n) for x, y in zip(a, b)])
# #zip(m,n)  [[[1,2,3],[2,2,2]],[[4,5,6],[3,3,3]],[[7,8,9],[4,4,4]]]
# #a,b a
#
#
# import copy
# list1 = [1, 2, [1, 2]]
#
# list2 = copy.copy(list1)
#
# print (list1==list2)
# print(list1 is list2)
#
#
# class test(object):
#     def __init__(self, value):
#         self.x = value
#
#     def __call__(self, value):
#         return self.x * value
#
# a = test(4)
# print(a.__call__(3))
# print (a(4))

def alph(str):
    str = "=" + str + "="
    for i in range(len(str)):
        if str[i].isalpha():
            if str[i+1] != "+" or str[i-1] != "+":
                return "false"
    return "true"

print(alph("+f+=+f+e+"))