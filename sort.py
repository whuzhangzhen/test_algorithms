#coding:utf-8

'''
author:zhangzhene
time:2017-6-15
'''

def insert_sort(lists):
    #插入排序
    count=len(lists)
    for i in range(1,count):
        key=lists[i]
        j=i-1
        while j>=0:
            if lists[j]>key:
                lists[j+1]=lists[j]
                lists[i]=key
            j-=1
    return lists

def  bubble_sort(lists):
    #冒泡排序
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists

def quick_sort(lists,left,right):
    #快速排序
    if left>=right:
        return lists
    key=lists[left]
    low=left
    high=right
    while left<right:
        while left<right and lists[right]>=key:
            right-=1
        lists[left]=lists[right]
        while left<right and lists[left]<=key:
            left+=1
        lists[right]=lists[left]
    lists[right]=key
    quick_sort(lists,low,left-1)
    quick_sort(lists,left+1,high)
    return lists


def select_sort(lists):
    #选择排序
    count=len(lists)
    for i in range(0,count):
        min=i
        for j in range(i+1,count):
            if lists[min]>lists[j]:
                min=j
        lists[min],lists[i]=lists[i],lists[min]
    return lists


def merge(left,right):
    #归并过程
    i,j=0,0
    result=[]
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    result+=left[i:]
    result+=right[j:]
    return result

def merge_sort(lists):
    #调用归并过程归并排序
    if len(lists)<=1:
        return lists
    num=len(lists)/2
    left=merge_sort(lists[:num])
    right=merge_sort(lists[num:])
    return merge(left,right)


test_list=[1,4,2,7,10]
s1=insert_sort(test_list)
s2=bubble_sort(test_list)
s3=select_sort(test_list)

print s1,s2,s3
