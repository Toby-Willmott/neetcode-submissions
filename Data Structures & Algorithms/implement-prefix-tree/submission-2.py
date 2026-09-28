class TrieNode:
    def __init__(self): 
        self.children = {}
        self.endOfWord = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()        

    def insert(self, word: str) -> None:
        cur = self.root
        for letter in word: 
            if letter not in cur.children: 
                cur.children[letter] = TrieNode()
            cur = cur.children[letter] 
        cur.endOfWord = True 
                
    def search(self, word: str) -> bool:
        cur = self.root 
        for letter in word: 
            if cur.children == {}: 
                return False
            if letter in cur.children:
                cur = cur.children[letter]
            else: 
                return False
        if cur.endOfWord == True: 
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.root 
        for letter in prefix: 
            if cur.children == {}: 
                return False
            if letter in cur.children:
                cur = cur.children[letter]
            else: 
                return False
        return True

        
        