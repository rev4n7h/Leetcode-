class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        arr = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max(candies):
               arr.insert(i,True)
            
            else :
               arr.insert(i,False)
        return arr

        