class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        s_dict = {}
        t_dict = {}

        for i in range(len(s)):
            current_s = s[i]
            current_t = t[i]

            if current_s in s_dict:
                s_dict[current_s] += 1
            else:
                s_dict[current_s] = 1

            if current_t in t_dict:
                t_dict[current_t] += 1
            else:
                t_dict[current_t] = 1
        
        for letter in s_dict:
            try: 
                if s_dict[letter] != t_dict[letter]:
                    return False
            except:
                return False
        return True


        

        