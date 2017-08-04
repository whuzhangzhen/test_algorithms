'''
字典树（Trie树）的实现
'''

class TrieNode(object):
    def __init__(self):
        self.data={}
        self.is_word=False

class Trie(object):
    def __init__(self):
        self.root=TreeNode()

    def insert(self,word):
       """
        Inserts a word into the trie.
         :type word: str
         :rtype: void
       """
        node =self.root
        for letter in word:
            child=node.data.get(letter)
            if not child:
                node.data[letter]=TrieNode()
            node=node.data[letter]
        node.is_word=True
            

    def search(self,word):
        node=self.root
        for letter in word:
            node=node.data.get(letter)
            if not node:
                return False
        return node.is_word

    def star_tWith(self,Prefix):
        node=self.root
        for letter in Prefix:
            node=node.data.get(letter)
            if not node:
                return False
        return True
        






