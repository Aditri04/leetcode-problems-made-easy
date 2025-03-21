class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
       
        if k == 0:
            return [0 for i in range(len(code))]
        sol = []
        n = len(code)
        winsum = 0
        if k>0:
            for i in range(k):
                winsum+=code[(i+1)%n]
            for i in range(n):
                sol.append(winsum)
                winsum-=code[(i+1)%n]
                winsum+=code[(i+1+k)%n]
        if k<0:
            for i in range(abs(k)):
                print(i-abs(k))
                winsum+=code[(i-abs(k))%n]
            for i in range(n):
                sol.append(winsum)
                winsum-=code[(i-abs(k))%n]
                winsum+=code[i]
        return sol 