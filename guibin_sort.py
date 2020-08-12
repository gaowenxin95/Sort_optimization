# -*- coding: utf-8 -*-
# @Time    : 2020/8/12 10:14
# @Author  : wenxin Gao
# @Email   : unique.gaowenxin@foxmail.com
# @File    : guibin_sort.py
# @Software: PyCharm

#两种方式实现
# -*- coding:utf-8 -*-
#算法逻辑比较简单，以第一个list为基准，第二个向第一个插空

'''

归并排序是一种递归算法，它持续地将一个列表分成两半。如果列表是空的或者 只有一个元素，那么根据定义，
它就被排序好了（最基本的情况）
。如果列表里的元素超过一个，我们就把列表拆分，然后分别对两个部分调用递归排序。一旦这两个部分被排序好了，
然后就可以对这两部分数列进行归并了。归并是这样一个过程：把两个排序好了的列表结合在一起组合成一个单一的有序的新列表。
有自顶向下（递归法）和自底向上的两种实现方法。

'''
# 在此之前需要先把list1和list2划分出来

def merge_sort(list1,list2):
    length_list1=len(list1)
    length_list2=len(list2)
    list3=[]
    j=0
    for i in range(length_list1):
        while j<length_list2 and list2[j]<list1[i]:
            list3.append(list2[j])
            j=j+1
        list3.append(list1[i])
    if j<(length_list2-1):
        for k in range(j,length_list2):
            list3.append(list2[k])
    return list3
#测试
list1=[1,3,5,10]
list2=[2,4,6,8,9,11,12,13,14]
print(merge_sort(list1,list2))


# 方法二

# 更充分的体现分治之的思想

def merge(left, right):
    res = []
    while left and right:
        min_val = left.pop(0) if left[0] < right[0] else right.pop(0)
        res.append(min_val)
    res += left if left else right
    return res


def merge_sort(A): #对半划分
    if len(A) <= 1:
        res = A
    else:
        mid = len(A) // 2
        left, right = merge_sort(A[:mid]), merge_sort(A[mid:])
        res = merge(left, right)
    return res