#coding:utf-8

class Queue:
    #构造函数
    def __init__(self):
        self.items=[]
    #判断队列是否为空
    def isEmpty(self):
        return self.items==[]
    #队列尾部添加元素
    def enqueue(self,item):
        self.items.insert(0,item)
    #队列头部删除元素
    def dequeue(self):
        self.items.pop()
    #返回队列长度
    def size(self):
        return len(self.items)



q=Queue()
q.enqueue(1)
q.enqueue('dog')
q.enqueue(True)

print q.size()

q.dequeue()
print q.items