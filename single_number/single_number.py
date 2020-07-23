'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # Your code here

    # Create an element of the array res as arr[0]
    res = arr[0]

    # Loop through the array starting after arr[0] which would be range starting at 1
    for i in range(1, len(arr)):
        # Create an instance of XOR (^), where XOR will not return any duplicates found in the list
        # Example: 1 ^ 2 ^ 2 ^ 3 ^ 1 will return 3
        res = res ^ arr[i]

    # Return res
    return res


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
