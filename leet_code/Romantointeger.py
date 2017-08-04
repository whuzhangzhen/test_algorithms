#coding:utf-8
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        sum1=0
        for i in range(0,len(s)-1):
            if roman[s[i]]<roman[s[i+1]]:
                sum1-=roman[s[i]]
            else:
                sum1+=roman[s[i]]

        return sum1+roman[s[-1]]
