import math

class Solution:
    '''
    Given a sorted array, This function return the index if the target is found. 
    Else, it returns -1.
    '''
    def search(self, arr:list, target:int)->int:
        left =0
        right = len(arr) - 1 
        
        while left <= right:
        
            mid = self.mid(left, right)
            if arr[mid] == target:
                return mid 
            else:
                if arr[mid] > target:
                    right = mid-1
                else:
                    left = mid+1
                
        return -1

    '''
    Given the left and right indies, this function finds the middle index.
    '''
    def mid(self, left:int, right:int): 
        return math.floor((left + right) / 2)
    
solution = Solution()
arr = [0, 1, 2, 3, 7, 10]
print(solution.search(arr, 3))