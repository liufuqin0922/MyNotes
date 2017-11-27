class TrieNode(object):
    def __init__(self, _child=None,_inter=None):
        child=list(_child)
        inter=_inter

class Trie(object):
    def __init__(self,_Node=TrieNode()):
        Node=_Node
        worldSum=0
    def insertDict(self, root,word,inter):
        wordlen=len(word)
        index=0
        if wordlen:
            return
        index=ord(word[0])
        #word=word[1:]
        if wordlen >1:
            if root.child[index] is not None:
                self.insertDict(root.child[index],word[1:],inter)
                else:
                    root.child[index]=TrieNode()
                    self.insertDict(root.child[index],word[1:],inter)
        elif wordlen ==1:
            if root.child[index] is not None:
                if root.child[index].inter is None:
                    root.child[index].inter=inter
                    return
                else:
                    return
            else:
                root.child[index]=TrieNode()
                root.child[index].inter=inter
                
        def createDict(self):
            wordNumber=0
            with open("raw-dict", "r") as f:
                for line in f:
                    word=line.strip()
                    inter=next(f)
                    wordNumber+=1
                    self.insertDict(self.Node,word,inter)
            print('*****Total number of words is %d.*****\n', wordNumber)
        def query(needToQuertWord):
            index=0;
                    

                
            
