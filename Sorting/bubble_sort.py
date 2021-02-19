def bubble_sort(nums):
    j = len(nums)-1
    step = 0
    while j > 0:
        for i in range(j):
            if nums[i] > nums[i+1]:
                swap(nums, i, i+1)
        j = j - 1
        step = step + 1
        print("Step " + str(step) + ": " + str(nums))
    return nums


def swap(nums, i, j):
    tmp = nums[j]
    nums[j] = nums[i]
    nums[i] = tmp

print("------\nTest 1\n------")
nums = [5, 4, 3, 2, 1]
print("Input: " + str(nums))
sorted_nums = bubble_sort(nums)
print("Sorted list: " + str(sorted_nums))

print("------\nTest 2\n------")
nums = [5, 4, 20, 3, 2, 1, -1, 0, 55, 4, 7, 8]
print("Input: " + str(nums))
sorted_nums = bubble_sort(nums)
print("Sorted list: " + str(sorted_nums))

print("------\nTest 3\n------")
nums = [-100, 1, 1, 1, 1]
print("Input: " + str(nums))
sorted_nums = bubble_sort(nums)
print("Sorted list: " + str(sorted_nums))

print("------\nTest 4\n------")
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Input: " + str(nums))
sorted_nums = bubble_sort(nums)
print("Sorted list: " + str(sorted_nums))

print("------\nTest 5\n------")
nums = [1]
print("Input: " + str(nums))
sorted_nums = bubble_sort(nums)
print("Sorted list: " + str(sorted_nums))