class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()        # Removes extra spaces automatically
        words.reverse()          # Reverse word order
        return " ".join(words)   # Join with single space