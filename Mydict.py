class TrieNode(object):
    def __init__(self, _child=None,_inter=None):
        child=list(_child)
        inter=_inter

class Trie(object):
    def __init__(self,_Node=None):
        Node=_Node
        worldSum=0
    def insertDict(self, root,word,inter):
        wordlen=len(word)
        index=0
        if wordlen:
            return
        index=