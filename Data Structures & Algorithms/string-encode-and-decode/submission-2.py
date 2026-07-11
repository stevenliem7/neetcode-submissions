class Solution:

    def encode(self, strs: List[str]) -> str:
        payload = ""
        for word in strs:
            payload += f"{len(word)}#{word}"
        return payload

    def decode(self, s: str) -> List[str]:
        payload = []
        # 10#HelloWorld5#World
        i=0
        while i < len(s):
            temp_count = i
            while s[temp_count] != "#" :
                temp_count += 1
            substring_counter = int(s[i:temp_count])
            payload.append(s[i+len(str(substring_counter)) + 1: i+substring_counter+len(str(substring_counter))+1])
            i += substring_counter + len(str(substring_counter)) + 1

        return payload

