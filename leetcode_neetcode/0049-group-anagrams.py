class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        frequency_dict = {}

        for item in strs:
            letter_count = [0] * 26
            for char in item:
                letter_count[ord(char)-ord("a")] += 1

            letter_tuple = tuple(letter_count)

            if letter_tuple in frequency_dict:
                frequency_dict[letter_tuple].append(item)
            else:
                frequency_dict[letter_tuple] = [item]
            

        return list(frequency_dict.values())    