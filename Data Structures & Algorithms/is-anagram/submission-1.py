class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        s_dict = {}
        t_dict = {}
        for word in s:
            if word in s_dict:
                s_dict[word] += 1
            else:
                s_dict[word] = 1

        for word in t:
            if word in t_dict:
                t_dict[word] += 1
            else:
                t_dict[word] = 1
        
        for letter in s_dict:
            try: 
                if s_dict[letter] != t_dict[letter]:
                    return False
            except:
                return False
        return True


        

        