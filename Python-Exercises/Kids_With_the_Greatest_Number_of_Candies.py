'''
Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.

For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number 
of candies among them. Notice that multiple kids can have the greatest number of candies.

'''

def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
        
    summary = [''] * len(candies)
        
    for i in range(len(candies)):
            
        candies[i] = candies[i] + extraCandies
            
        if candies[i] == max(candies):
            summary[i] = (True) 
            
        else: 
            summary[i] = False
                
       	candies[i] = candies[i] - extraCandies
                    
    return summary




