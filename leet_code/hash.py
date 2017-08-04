#coding:utf-8
'''
time:2017-7-15
@anthor:zhangzhen
'''

class Soulution(object):
    #id:136 Single Number
    #Given an array of integers, every element appears twice except for one. Find that single one.
    def singleNumber(self,nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
        count={}
        for item in nums:
            count[item]=count.get(item,0)+1
        for i in count:
            if count[i]==1:
                return i
        

