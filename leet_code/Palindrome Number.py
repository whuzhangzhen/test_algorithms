#coding:utf-8
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            return False
        else:
            x1=int(`x`[::-1])
            return x-x1==0