#coding:utf-8
'''
def printInc(n):
    if n>0:
        print n
        printInc(n-1)
'''




def fib(n):
    assert n >=1
    if n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

#printInc(6)
s=fib(5)
print s