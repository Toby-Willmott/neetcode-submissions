class PrefixTree: 
    def __init__(self): 
        self.children = {}
        self.end_word = False

class WordDictionary:

    def __init__(self):
        self.root = PrefixTree()

    def addWord(self, word: str) -> None:
        cur = self.root
        for letter in word: 
            if letter not in cur.children:
                cur.children[letter] = PrefixTree()
            cur = cur.children[letter]
        cur.end_word = True
        
    def search(self, word: str) -> bool:
        def dfs(j, root): 
            cur = root

            for i in range(j, len(word)): 
                if word[i] == ".": 
                    for child in cur.children.values(): 
                        if dfs(i+1, child): 
                            return True
                    return False
                else: 
                    if word[i] not in cur.children: 
                        return False
                    cur = cur.children[word[i]] 
            return cur.end_word 
        return dfs(0, self.root)
        
