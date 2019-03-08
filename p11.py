# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.
#
# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
#
# Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
from collections import defaultdict


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, word):
        current_node = self.root
        for i in range(len(word)):
            if word[i] in current_node.children:
                current_node = current_node.children[word[i]]

            else:
                current_node.children[word[i]] = Node()
                current_node = current_node.children[word[i]]

            if i == len(word) - 1:
                current_node.value = word
                return

    def find(self, query):
        current_node = self.root

        i = 0
        while i < len(query):
            if current_node.children[query[i]]:
                current_node = current_node.children[query[i]]
            else:
                return []
        return self.accumulate(current_node)


    def accumulate(self, root):
        if root != None:
            autocomplete = []
            for char in root.children:
                autocomplete.append(self.accumulate(char))
            return root.value
        return None



class Node:
    def __init__(self, value=None, children={}):
        self.value = value
        self.children = children


def query_dict(word):
    wordz = set()
    for entry in WORDS:
        if entry.startswith(word):
            wordz.add(entry)
    return wordz

def preprocess_dict(lst):
    preprocessed = defaultdict(list)
    for word in lst:
        for i in range(len(word)):
            if i == len(word) - 1:
                subtext = word[0:]
            else:
                subtext = word[0: i + 1]
            preprocessed[subtext].append(word)
    return preprocessed

def query_dictionary(lst, query):
    return lst[query]

WORDS = ['foo', 'bar', ...]
def autocomplete(s):
    results = set()
    for word in WORDS:
        if word.startswith(s):
            results.add(word)
    return results

def main():
    dictionary = ["dog", "deer", "deal"]

    # efficient_dictionary = preprocess_dict(dictionary)
    # tada = query_dictionary(efficient_dictionary, "de")
    #
    # print("hello")
    trie = Trie()

    for word in dictionary:
        trie.add(word)

    autocompleted = trie.find("de")

main()

ENDS_HERE = '__ENDS_HERE'


class Trie(object):
    def __init__(self):
        self._trie = {}

    def insert(self, text):
        trie = self._trie
        for char in text:
            if char not in trie:
                trie[char] = {}
            trie = trie[char]
        trie[ENDS_HERE] = True

    def elements(self, prefix):
        d = self._trie
        for char in prefix:
            if char in d:
                d = d[char]
            else:
                return []
        return self._elements(d)

    def _elements(self, d):
        result = []
        for c, v in d.items():
            if c == ENDS_HERE:
                subresult = ['']
            else:
                subresult = [c + s for s in self._elements(v)]
            result.extend(subresult)
        return result

trie = Trie()
for word in words:
    trie.insert(word)

def autocomplete(s):
    suffixes = trie.elements(s)
    return [s + w for w in suffixes]