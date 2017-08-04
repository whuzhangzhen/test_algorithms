#coding:utf-8



#二叉树的实现
class BinaryTree:
    #构造函数
    def __init__(self,rootObj):
        self.key=rootObj
        self.leftChild=None
        self.rightChild=None
    #插入左节点
    def insertLeft(self,newNode):
        if self.leftChild==None:
            self.leftChild=BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.leftChild=self.leftChild
            self.leftChild=t
    #插入右节点
    def insertRight(self,newNode):
        if self.rightChild==None:
            self.rightChild=BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.rightChild=self.rightChild
            self.rightChild=t
    #获取左节点
    def getLeft(self):
        return self.leftChild
    #获取右节点
    def getRight(self):
        return self.rightChild
    #设置根节点
    def setRootVal(self,obj):
        self.key=obj
    #获取跟节点
    def getRootVal(self):
        return self.key