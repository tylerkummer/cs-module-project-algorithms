'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):

    # Your code here
    # Create a value for len of list
    n = len(nums)
    # Create an empty results list
    results = []
    # Traverse the list with the range of nums minus our k adding 1
    for i in range(n - k + 1):
        # Set max_value to our current index
        max_value = nums[i]
        # Traverse the list up to k
        for j in range(1, k):
            # Check if our index of i + j is greater than our current index
            if nums[i + j] > max_value:
                # Set the max value to the next index of i + j
                max_value = nums[i + j]
        # Append the array of results then return it
        results.append(max_value)
    return results


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
