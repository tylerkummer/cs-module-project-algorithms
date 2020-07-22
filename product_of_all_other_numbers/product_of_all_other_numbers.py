'''
Input: a List of integers
Returns: a List of integers
'''


def product_of_all_other_numbers(arr):
    # Your code here

    # The length of the input array
    n = len(arr)

    # Create the left right and answer arrays
    l = [0]*n
    r = [0]*n
    ans = [0]*n

    # l[i] contains the product of all the elements to the left
    l[0] = 1
    # Construct the left array
    for i in range(1, n):
        # l[i - 1] has the product of elements to the left of 'i - 1' and nums[i - 1] would give the product of all  elements to the left of index 'i'
        l[i] = arr[i - 1] * l[i - 1]

    # r[i] contains the product of all the elements to the right
    r[n - 1] = 1
    # Construct the right array
    for i in reversed(range(n - 1)):
        # r[i + 1] already contains the product of elements to the right of 'i + 1' multiplying it with nums[i + 1] would give the product of all elements to the right of index 'i'
        r[i] = arr[i + 1] * r[i + 1]

    # Constructing the answer array
    for i in range(n):
        # For the first element, r[i] would be product except for itself
        ans[i] = l[i] * r[i]

    return ans


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8,
           9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
