<h1>Binary Search</h1>

In each attempt, binary search exclude half of the input to deduce the time complexity.

<h2>Algorithm</h2>
The array has to be sorted.<br> 

1. find the middle <br>
2. Check if the middle is equal to the target<br>
3. If the middle is equal to the target, search is completed <br>
4. If the middle is not equal to the garget, continue the search. <br>
If the target is greater than the middle, search the right half.<br> 
If the target is less than the middle, search the left half.<br>

<h2>Recursive implementation</h2>

<h3>Time complexity</h3>
n = number of elements <br>
Time complexity is the number of times needed to divide in half to reach the unit. <br>
Time complexity = O(log n) <br>

<h3>Space complexity</h3>
n = number of elements <br>
The space complexity is also proportional to the number of times needed to divide in half to reach the unit. <br>
Ex <br>
each level has to be saved on the recursion stack.<br>

Space complexity = O(log n) <br>

<h2>Iterative implementation</h2>

<h3>Time complexity</h3>
The same as the recursive implementation.

<h3>Space complexity</h3>
Depends on the space taken by left and right which is a constant<br>

Space complexity = O(1) <br>
