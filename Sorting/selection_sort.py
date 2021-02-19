def selection_sort(nums):
    step = 0
    for i in range(len(nums)):
        min_index = i
        # update minimum value by going through the list
        for j in range(i, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j

        # swap the minimum value and the value at i
        if i != min_index:
            swap(nums, i, min_index)
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
sorted_nums = selection_sort(nums)
print("Sorted list: " + str(sorted_nums))

print("------\nTest 2\n------")
nums = [5, 4, 20, 3, 2, 1, -1, 0, 55, 4, 7, 8]
print("Input: " + str(nums))
sorted_nums = selection_sort(nums)
print("Sorted list: " + str(sorted_nums))

print("------\nTest 3\n------")
nums = [-100, 1, 1, 1, 1]
print("Input: " + str(nums))
sorted_nums = selection_sort(nums)
print("Sorted list: " + str(sorted_nums))

print("------\nTest 4\n------")
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Input: " + str(nums))
sorted_nums = selection_sort(nums)
print("Sorted list: " + str(sorted_nums))

print("------\nTest 5\n------")
nums = [1]
print("Input: " + str(nums))
sorted_nums = selection_sort(nums)
print("Sorted list: " + str(sorted_nums))