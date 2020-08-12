'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    newArr = []
    for i in arr:               # loop through given array
        if i in newArr:         # if the current number already
            newArr.remove(i)    # remove it from new Array
        else:
            newArr.append(i)    #if the number does not exist add it to newArr
    return newArr[0]



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")