'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # Your code here

    # Create a counter for non zero elements
    count = 0

    # Traverse the list
    for i in range(len(arr)):
        # Check for non zero elements then replace the index of the element with count, and increment count at the end
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1

    # All Non zero elements are shifted to the front
    while count < len(arr):
        # Set arr[count] to index of zero and increment count, to move the elements 0 to the end
        arr[count] = 0
        count += 1

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
