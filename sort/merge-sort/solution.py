class Solution:
    '''
    This function sort the given array by using the merge sort 
    algorithm.
    '''
    def sort(self, a):
        if len(a) == 1:
            return 

        left, right = self.divide(a)
        self.sort(left)
        self.sort(right)
        self.merge(a, left, right)

    '''
    This function divides the given array into two parts.
    '''
    def divide(self, a:list):
        left = a[:len(a)//2]
        right = a[len(a)//2:]

        return (left, right)
    
    '''
    This function merge two given arrays so that the resulting array is
    also sorted.
    '''
    def merge(self, a:list, left:list, right:list)->list:
        #left=[6] right=[5]
        i =0
        j =0
        k =0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1
            k += 1
        #if there is any element left in the left array, add it to the result
        while i < len(left):
            a[k] = left[i]
            i += 1
            k += 1

        #if there is any element left in the right array, add it to the result
        while j < len(right):
            a[k] = right[j]
            j += 1
            k += 1
        
solution = Solution()
a = [2, 6, 5, 1, 7, 4, 3]
solution.sort(a)
print(a)