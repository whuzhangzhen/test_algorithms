#coding:utf-8

class solution(object):
    def twoSum(self,nums,target):
        '''

        :param nums:
        :param target:
        :return:
        '''
        result=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    result=[i,j]
                    break

        return result

example=solution()
ss=example.twoSum([1,2,3],5)
print ss