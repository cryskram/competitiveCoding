# failed + didnt complete


class Solution:
    def findWords(self, words: list) -> list:
        dum = []
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        for word in words:
            word = word.lower()
            for i in range(len(word) - 1):
                if word[i] in row1:
                    continue
