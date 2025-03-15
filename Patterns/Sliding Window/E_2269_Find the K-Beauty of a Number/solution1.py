class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        kbeautynumber = 0
        numstr=str(num)
        numwinstr = ''
        for i in range(len(numstr)):
            if i <k-1:
                numwinstr+=numstr[i]
                continue
            else:
                numwinstr+=numstr[i]
                numwin = int(numwinstr)
                if numwin!=0 and num%numwin==0:
                    kbeautynumber+=1
                numwinstr = numwinstr[1:]
        return kbeautynumber
            
                