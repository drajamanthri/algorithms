<h1>Bubble Sort</h1>
Bubble sort has two loops. The outer loop runs n times. The inner loop runs the following number of times on each pass. <br>
<code>
n, n-1, n-2, .., 1
</code>
<br>
On each pass, the largest or the next largest element is bubbled up.<br>

<h2>Time complexity</h2>
<code>
1 + 2 + .. + n = n * (n+1)/2
</code>
<br>
Time complexity = O(n^2)

<h2>Space complexity</h2>
The space complexity depends on the space taken by i, j, and temp which is a constant.
<br>
Space complexity = O(1)