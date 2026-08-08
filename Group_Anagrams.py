import string
class Solution:
    def Group_of_Anagrams(self,strs):
        i = 0
        alphabet_order = {}
        for lower_case_alphabet in string.ascii_lowercase:
            alphabet_order[lower_case_alphabet] = i
            i += 1
        final_list = {}
        for word in strs:
            alphabet_structure = [0] * 26
            for letter in word:
                alphabet_structure [alphabet_order[letter]] += 1
            alphabet_structure =  tuple(alphabet_structure)
            if alphabet_structure in final_list:
                final_list[alphabet_structure].append(word)
            elif alphabet_structure not in final_list:
                final_list[alphabet_structure] = []
                final_list[alphabet_structure].append(word)
        return list(final_list.values())
