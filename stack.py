#coding:utf-8

class Stack:
    #构造方法
    def __init__(self):
        self.items=[]
    #判断栈是否为空
    def isEmpty(self):
        return self.items==[]
    #入栈
    def push(self,item):
        self.items.append(item)

    #出栈
    def pop(self,item):
        self.items.pop()

    #返回栈顶元素
    def peek(self):
        return self.items[len(self.items)-1]

    #返回栈的深度
    def size(self):
        return len(self.items)

