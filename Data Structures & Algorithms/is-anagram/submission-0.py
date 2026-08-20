class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts1 = {}
        for letter in s:
            counts1[letter] = counts1.get(letter, 0) + 1

        counts2 = {}
        for letter in t:
            counts2[letter] = counts2.get(letter, 0) + 1

        if counts1 == counts2:
            return True
        return False