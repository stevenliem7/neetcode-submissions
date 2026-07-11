class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Map of lists that stores length of characters of that particular word based on length?
        global_map = {}
        for word in strs:
            temp = {}

            for letter in word:
                if letter not in temp:
                    temp[letter] = 1
                else:
                    temp[letter] += 1
            
            fs = tuple(sorted(temp.items()))
            if fs not in global_map.keys():
                global_map[fs] = [word]
            else:
                global_map[fs].append(word)
                
        return list(global_map.values())


        