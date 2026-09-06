class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        arr = []
        mc = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= mc:
               arr.insert(i,True)
            
            else :
               arr.insert(i,False)
        return arr

        