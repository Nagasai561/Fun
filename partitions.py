# This function takes in two parameters 'n' and 'k' (n,k > 0)
# This returns the list of all partitions (represented as lists) whose individual parts are <= k
# Moreover the each partition is in non-decreasing order

def partition_helper(n, k):
    res = []    # initializing an empty list to store all our partitions
    if(k == 1):     # If k == 1 then there is only one way to partition i.e [1,1,1....] (n times)
        res.append([1 for i in range(n)])
        return res
    
    # let i be the maximum element in a particular partition
    # Then all other elements other than it is a partition of 'n-i'
    # and the largest element will be atmax 'n'

    # We will use the above idea and iterate over all possible 'i'
    # Make sure to take care of corner cases
    for i in range(1, min(k, n-1)+1):  
        for xs in partition_helper(n-i, i):
            y = xs.copy()
            y.append(i)
            res.append(y)

    # If n <= k, even [n] is valid partition, so we will include it too
    if(n <= k):
        res.append([n])
    
    return res


# Let's abstract away all unnecessary details above function
# So, we create a new function, which takes in a positive integer and returns it's partitions
def partitions(n):
    return partition_helper(n, n)
