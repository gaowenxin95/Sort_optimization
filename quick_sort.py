# -*- coding: utf-8 -*-
# @Time    : 2020/8/12 9:09
# @Author  : wenxin Gao
# @Email   : unique.gaowenxin@foxmail.com
# @File    : quick_sort.py
# @Software: PyCharm

## 快速排序

def quick_sort(arr):
    """快速排序"""
    if len(arr) < 2:
        return arr
    # 选取基准，随便选哪个都可以，选中间的便于理解
    mid = arr[len(arr) // 2]
    # 定义基准值左右两个数列
    left, right = [], []
    # 从原始数组中移除基准值
    arr.remove(mid)
    for item in arr:
        # 大于基准值放右边
        if item >= mid:
            right.append(item)
        else:
            # 小于基准值放左边
            left.append(item)
    # 使用迭代进行比较
    return quick_sort(left) + [mid] + quick_sort(right)



test=[14,5,6,2,8,6,4,7,12,45,2,1,22]
print(quick_sort(test))


# 上面是基础算法

# 还是要多找一些应用