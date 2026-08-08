from collections import defaultdict
import  string
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        all_strs_with_dict = defaultdict(list)
        letters = string.ascii_lowercase
        string_dict = {}
        i = 0
        for letter in letters:
            string_dict[letter] = i
            i += 1
        for word in strs:
            word_list = [0] *26
            for each_letter in word:
                word_list[string_dict[each_letter]] = word_list[string_dict[each_letter]] + 1
            all_strs_with_dict[word] = word_list
        modified_dict = {}
        for word in strs:
            if tuple(all_strs_with_dict[word]) in modified_dict:
                modified_dict[tuple(all_strs_with_dict[word])].append(word)
            elif tuple(all_strs_with_dict[word]) not in modified_dict:
                modified_dict[tuple(all_strs_with_dict[word])] = []
                modified_dict[tuple(all_strs_with_dict[word])].append(word)
        output = []
        for word in modified_dict:
            output.append(modified_dict[word])
        return output
