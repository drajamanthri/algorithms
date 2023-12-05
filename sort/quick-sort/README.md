<h1>Quick Sort</h1>
<h2>Time complexity</h2>
<code>
<pre>
number of steps = n * number of levels (number of times it takes to divide the problem so that it can not be further divided).
number of steps = n log(n)

complexity = O(n log(n))
</pre>
</code>

<h2>Space Complexity</h2>
<h3>Not considering the recursive stack</h3>
<code>
Space complexity = O(1)
</code>
<br>
This is because we are using constant space for pointers and no additional space. Sorting is done inline.

<h3>Considering the recursive stack</h3>
We recursively partition until we reach a single element.<br>
Therefore the, <br>
<code>
space complexity = O(n)
</code>
