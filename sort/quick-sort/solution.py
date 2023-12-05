
class Solution:
    '''
    This function sorts a list by using the quick sort algorithm
    '''
    def sort(self, l:list, low:int, high:int):
        if low < high:

            pivot_i = self.partition(l, low, high)

            #sort the left of the mid
            self.sort(l, low, pivot_i - 1)
            #sort the right of the mid

            self.sort(l, pivot_i+1, high)

    '''
    This function pick a value called the pivot and place it at the right position.
    After positioning the pivot, all the values to the left of the pivot is less than the pivot and
    all the values to the right of the pivot is greater than the pivot.
    '''
    def partition(self, l:list, low:int, high:int):
        #we choose the high index as the pivot
        pivot_i = high     
        pivot = l[pivot_i] 
        #filter the values less than the pivot to the left
        #filter the values greater than the pivot to the right
        
        i = low       #i = left pointer
        j = high - 1  #j = right pointer

        while i < j: #repeat the following steps until i < j
            #move the left pointer to the next larger value from the left
            while l[i] < pivot and i < j:
                i += 1

            #move the right pointer to the next smaller value from the right
            while l[j] > pivot and i < j: 
                j -= 1                    

            #if the left value is greater than the right value, swap them.
            if l[i] >= l[j] and i < j: 
                (l[j], l[i]) = (l[i], l[j])

        #finally all the values to the left of i is less than the pivot
        #if value(i) is less than the pivot, swap the value(i) and pivot
        #in this case, we need to update the pivot index.
        if l[i] > l[pivot_i]:
            (l[pivot_i], l[i]) = (l[i], l[pivot_i])
            pivot_i = i

        #now all the values to the right of i is larger than the pivot
        #pivot is at the right position
        return pivot_i


s = Solution()
l = [10, 16, 8, 12, 15, 6, 3, 9, 5]

s.sort(l, 0, 9)

print(l)