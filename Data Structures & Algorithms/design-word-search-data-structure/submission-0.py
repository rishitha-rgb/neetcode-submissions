class TrieNode:
    def __init__(self):
        self.children = {}    
        self.is_end = False   

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def search(self, word: str) -> bool:
        return self.dfs(self.root, word, 0)
    
    def dfs(self, node: TrieNode, word: str, index: int) -> bool:
        if index == len(word):
            return node.is_end  
        
        char = word[index]
        if char == '.':
            for child_node in node.children.values():
                if self.dfs(child_node, word, index + 1):
                    return True
            return False
        else:
            if char not in node.children:
                return False
            return self.dfs(node.children[char], word, index + 1)