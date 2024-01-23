class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        res = []
        p_counter = Counter(p) 
        window_counter = Counter(s[:k]) 

        if p_counter == window_counter:
            res.append(0)

        for i in range(len(s)-k): 
            window_counter[s[i]] -= 1

            if window_counter[s[i]]==0:
                del window_counter[s[i]]

            window_counter[s[i+k]] += 1

            if window_counter == p_counter:
                res.append(i+1)
        
        return res