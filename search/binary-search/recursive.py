import math

class Solution:
    '''
    This function return the index if the target is found. 
    Else, it returns -1.
    '''
    def search(self, arr:list, target:int)->int:
        left =0
        right = len(arr) - 1
        return self.binary_search(arr, left, right, target)

    '''
    Given a sorted array, left and right indices, this function search the target
    within the indices.
    '''
    def binary_search(self, arr:list, left:int, right:int, target:int)->int:
        if left > right:
            return -1
        
        mid = self.mid(left, right)
        if arr[mid] == target:
            return mid 
        else:
            if arr[mid] > target:
                return self.binary_search(arr, left, mid-1, target)
            else:
                return self.binary_search(arr, mid+1, right, target)

    '''
    Given the left and right indies, this function finds the middle index.
    '''
    def mid(self, left:int, right:int): 
        return math.floor((left + right) / 2)
    
solution = Solution()
arr = [0, 1, 2, 3, 7, 10]
print(solution.search(arr, 3))


