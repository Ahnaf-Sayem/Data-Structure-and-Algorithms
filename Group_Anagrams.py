from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp_of_anagrams=defaultdict(list)
        for word in strs:
            count=[0]*26
            for letter in word:
                count[ord(letter)-ord('a')]+=1
            grp_of_anagrams[tuple(count)].append(word)
        return list(grp_of_anagrams.values())


