#Maximum sum of consecutive Sub-array of fixed size k
#Traditional approach
'''
def max_sum(arr, k):
    n = len(arr)
    maxsum = 0
    for i in range(n - k + 1):
        add = 0
        for j in range(k):
            add += arr[i + j]
        maxsum = max(maxsum, add)
    return maxsum
print(max_sum([1, 2, 3, 4, 5], 3))
'''
#Optimal Solution
def max_sum(arr, k):
    maxsum2 = 0
    add2 = sum(arr[:k])
    for i in range(k, len(arr)):
        add2 = add2 - arr[i - k] + arr[i]
        maxsum2 = max(maxsum2, add2)
    return maxsum2
print(max_sum([1, 2, 3, 4, 5], 3))