class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        settemp = set()
        counter = 0
        for i in range(2,len(s)):
            if i>2:
                settemp.discard(s[i-3])
            settemp.add(s[i])
            settemp.add(s[i-1])
            settemp.add(s[i-2])
            
            
            if len(settemp)>=3:
                counter+=1
                
            
        return counter
                    