class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        points = 0
        suminwindow = 0
        for i in range(len(calories)):
            if i < k-1:
                suminwindow+=calories[i]
                continue
            else:
                suminwindow+=calories[i]
                if suminwindow<lower:
                    points-=1
                elif suminwindow>upper:
                    points+=1
                suminwindow-=calories[i-k+1]

        return points