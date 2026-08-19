s = 'hello world hello world spark hello spark python java python'

lst = s.split(' ')
print(lst)

kv = list(map(lambda tmp : {tmp : 1},lst))

from functools import reduce

def fun(dict1,dict2):
    """
    作用是给reduce当回调函数使用，将key相同的值相加（计算key的个数）
    :param dict1: 用作累加变量
    :param dict2: 加的变量
    :return:
    """
    key = list(dict2.items())[0][0]
    value = list(dict2.items())[0][1]
    dict1[key] = dict1.get(key,0) + value
    return dict1

re = reduce(fun,kv)
print(re)