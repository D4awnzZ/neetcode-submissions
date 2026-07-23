class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table ={}

        for s in strs:
            s_sorted = "".join(sorted(s))
            if s_sorted not in table:
                table[s_sorted] = [s]
            else:
                table[s_sorted].append(s)
        return list(table.values())

        