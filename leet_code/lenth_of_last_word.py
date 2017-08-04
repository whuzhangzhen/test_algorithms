#coding:utf-8
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        else:
            word_list = s.split()
            return len(word_list[-1])


test=Solution()
s='a '
length=test.lengthOfLastWord(s)
print length

