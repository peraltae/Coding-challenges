'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''
from _ast import List


class TwoSumSolutions:
    def __init__(self, nums: List[int], target):
        self.nums = nums
        self.target = target

    '''
    Enumerate solution was conceived by notes in the Two-Sum discussion page 
    link: https://leetcode.com/articles/two-sum/ 
    '''
    def enumerate(self, nums, target):

        checker = {}

        for i, num in enumerate(nums):

            # Find the compliment of the target and num at enumeration i
            compliment = target - num

            '''
			If the compliment of the target minus the current num isn't in the dictionary, then add it with the
			nums[i] as key and index as the value
			'''
            if compliment not in checker:
                checker[num] = i #if the compliment is not in the dict, then num:i is added

            else:
				#if the compliment does exist, then return the value for its key, and the current enumeration
                return [checker[compliment], i]



    #Brute force approach
	def bruteForce(self,nums,target):
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if nums[j] == target - nums[i]:
                        return [i,j]





