class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table = {}
        if len(s) != len(t):
            return False

        for chars in s:
            if chars not in table:
                table[chars] = 1
            else:
                table[chars] += 1
        for chart in t:
            if chart in table:
                table[chart] -= 1
        if all(val == 0 for val in table.values()):
            return True
        return False 
