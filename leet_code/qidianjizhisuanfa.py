#coding:utf-8

'''
 #第一题
'''
def ReverseWords(input):
    #转置字符串
    return input[::-1]
'''
 #第二题
'''

def count(input_list):
    #求列表的和
    sum=0
    for item in input_list:
        sum+=item
    return sum

def minindex(input_list,ix):
    #求离目标最小的元素
    distance={}
    for item in input_list:
        distance[item]=abs[item-ix]
    return min(distance.items(), key=lambda x: x[1])[0]


def minmum(input):
    #差值最小
    listA=[]
    listB=[]
    #得到相对差值最小的两组列表
    for i in input:
        if count(listA)>listB:
            listB.append(i)
        else:
            listA.append(i)

    for j in range(100):
        #记录迭代前的差值
        chazhi = abs(count(listA) - count(listB))

        if count(listA)>count(listB):
            listB.append(minindex(listA,(count(listA)-count(listB))/2))
            listA.remove(minindex(listA,(count(listA)-count(listB))/2))
        else:
            listA.append(minindex(listB,(count(listB)-count(listA))/2))
            listB.remove(minindex(listB,(count(listB)-count(listA))/2))
        #迭代后的差值和迭代前比较，如果相等则说明迭代稳定，跳出循环
        if abs(count(listA) - count(listB))==chazhi:
            break
    return listA,listB

'''
#第三题
'''
def mindistance(input):
    #点距离最小
    x=0
    y=0
    for item in input:
        x+=item[0]
        y+=item[1]

    return [x/len(input),y/len(input)]
