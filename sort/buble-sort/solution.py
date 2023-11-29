class Solution:
    '''
    This function sort the given array a by bubble sort.
    '''
    def sort(self, a:list):

        for i in range(len(a)):
            for j in range(len(a) - (i+1)):
                #compare a[j] and a[j+1]
                if a[j] > a[j+1]:
                    self.swap(a, j, j+1)

    '''
    This function swap two elements of an array. The indices of the two 
    elements are given by i and j.
    '''     
    def swap(self, a:list, i:int, j:int):
        temp = a[i]
        a[i] = a[j]
        a[j] = temp 

solution = Solution()
a = [5, 3, 8, 6, 7, 2]
solution.sort(a)

print(a)