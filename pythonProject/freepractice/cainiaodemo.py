#有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？C4 3
from random import shuffle

# !/usr/bin/python
# -*- coding: UTF-8 -*-

for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != k) and (i != j) and (j != k):
                print(i, j, k)

#一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？