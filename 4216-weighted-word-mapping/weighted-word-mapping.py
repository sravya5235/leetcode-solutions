class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:

        charWgt = lambda ch: weights[ord(ch) - 97]
        wordWgt = lambda word: chr(122 - sum(map(charWgt, word)) %26)

        return ''.join(map(wordWgt, words))