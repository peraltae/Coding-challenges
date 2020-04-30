'''
for this task, add two optimizations to the implementation of Bubble Sort.

1) Note that by the end of sweep X, Bubble Sort will have migrated the X largest items 
to their final correct positions at the top X highest slots in the array. So, there 
is no need for each sweep to work over the entire array: later sweeps can stop earlier. 

Figure out how to trip the inner loop with successive passes, but without affecting the accuracy of the sorting.

2) Bubble Sort has a very nice property: if the list is already partially sorted, Bubble Sort doesn’t need 
the entire N sweeps to sort N items. Specifically, it can stop the outer loop earlier under some conditions. 

Figure out what that condition is, and see if you can get it to run much faster on mostly-ordered arrays. 
On an array that is actually completely ordered, Bubble Sort should be able to stop after a single sweep.


'''



def bubble_sort(nums):

	sweep = 0
	end = len(nums) - 1

	for rounds in range(len(nums)):
		for i in range(end - sweep):
			print(end)

			if nums[i] > nums[i+1]:
				nums[i], nums[i + 1] = nums[i+1], nums[i]
				end = i+1	
		
		sweep += 1
		print(nums, "\n")

	print("\n", inner_count)


def main():
	f = [3,4,5,2,1]

	bubble_sort(f)

main()
