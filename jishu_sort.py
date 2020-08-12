# -*- coding: utf-8 -*-
# @Time    : 2020/8/12 9:35
# @Author  : wenxin Gao
# @Email   : unique.gaowenxin@foxmail.com
# @File    : jishu_sort.py
# @Software: PyCharm

# 计数排序

## 算法步骤


'''
1. 花O(n)的时间扫描一下整个序列 A，获取最小值 min 和最大值 max



2. 开辟一块新的空间创建新的数组 B，长度为 ( max - min + 1)



3. 数组 B 中 index 的元素记录的值是 A 中某元素出现的次数



4. 最后输出目标整数序列，具体的逻辑是遍历数组 B，输出相应元素以及对应的个数

'''


def count_sort(list):
	max=min=0
	for i in list:
		if i < min:
			min = i
		if i > max:
			max = i
	count = [0] * (max - min +1)
	for j in range(max-min+1):
		count[j]=0
	for index in list:
		count[index-min]+=1
	index=0
	for a in range(max-min+1):
		for c in range(count[a]):
			list[index]=a+min
			index+=1
	return list
	#测试：
list=[10,23,1,53,654,54,16,646,65,3155,546,31]
print count_sort(list)