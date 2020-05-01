'''
for this task, add two optimizations to the implementation of Bubble Sort.

1) Note that by the end of sweep X, Bubble Sort will have migrated the X largest items 
to their final correct positions at the top X highest slots in the array. So, there 
is no need for each sweep to work over the entire array: later sweeps can stop earlier. 

Figure out how to trip the inner loop with successive passes, but without affecting the accuracy of the sorting.
--> Continually deduct the number of rounds completed from the length of iteration of the inner for-loop

2) Bubble Sort has a very nice property: if the list is already partially sorted, Bubble Sort doesn’t need 
the entire N sweeps to sort N items. Specifically, it can stop the outer loop earlier under some conditions. 

Figure out what that condition is, and see if you can get it to run much faster on mostly-ordered arrays. 
On an array that is actually completely ordered, Bubble Sort should be able to stop after a single sweep.

--> Assume that the array is partially sorted, and continue swapping if a contridiction is found


'''



def bubble_sort(nums):


	outer_loop_count = 0
	inner_loop_count = 0
 

	for rounds in range(len(nums)):
		sorted = True

		for i in range(len(nums)-1-rounds):
			if nums[i] > nums[i+1]:
				nums[i], nums[i + 1] = nums[i+1], nums[i]
				sorted = False
				inner_loop_count += 1

		
		outer_loop_count += 1

		if(sorted):
			break



		

	#print statements for debugging
	print("outer-loops done:", outer_loop_count)
	print("inner-loops done:", inner_loop_count)
	print(nums, "\n")







