<h1>Merge sort</h1>
<h2>Algorithm</h2>
1. divide the array into 2 parts <br>
2. sort the left array <br>
3. sort the right array <br>
4. Merge 2 arrays so that the result is also sorted.<br>

<br>
Sorting is done recursively.

<h2>Time complexity</h2>
n = number of elements <br>

Time complexity = O(n log n) <br>
log n = the number of times needed to divide in half to reach the unit.<br>
n = time needed to merge on each step

<h2>Space complexity</h2>

Space complexity = O(n) <br>

This is the maximum memory used at any given time. At the time we reach the unit element, if we add up all the created arrays, it is proportional to n.

