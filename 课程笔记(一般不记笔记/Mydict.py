class TrieNode(object):
    def __init__(self, _child=None, _inter=None):
        if _child is None:
            self.child=[]
            for x in range(128):
                self.child.append(None)
        else:
            self.child = list(_child)
        self.inter = _inter


class Trie(object):
    def __init__(self):
        self.Node = TrieNode()
        self.worldSum = 0

    def insertdict(self, root, word, inter):
        wordlen = len(word)
        if wordlen is 0:
            return
        index = word[0]
        # word=word[1:]
        if wordlen > 1:
            if root.child[index] is not None:
                self.insertdict(root.child[index], word[1:], inter)
            else:
                root.child[index] = TrieNode()
                self.insertdict(root.child[index], word[1:], inter)

        elif wordlen == 1:
            if root.child[index] is not None:
                if root.child[index].inter is None:
                    root.child[index].inter = inter
                    return
                else:
                    return
            else:
                root.child[index] = TrieNode()
                root.child[index].inter = inter

    def createdict(self):
        self.worldSum = 0
        with open("raw-dict", "rb+") as f:
            for line in f:
                word = line.strip()
                inter = next(f).strip()
                self.worldSum += 1
                self.insertdict(self.Node, word, inter)
        print('*****Total number of words is %d.*****\n', self.worldSum)

    def query(self, word, root=None):
        if root is None:
            root = self.Node
        wordlen = len(word)
        if wordlen == 0 or root is None:
            print("This word is not exist")
            return
        index = ord(word[0])
        if wordlen == 1:
            if root.child[index] and root.child[index].inter:
                print(root.child[index].inter.decode('utf8'))
                return
            else:
                print("This word is not exist")
        else:
            self.query(word[1:], root.child[index])


if __name__ == '__main__':
    dictionaryTrie = Trie()
    dictionaryTrie.createdict()
    print('输入查询的单词，q退出')
    need_query_word=input("!!!--")
    while need_query_word is not 'q':
        dictionaryTrie.query(need_query_word)
        need_query_word = input("!!!|--|")

