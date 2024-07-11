### Twice Linear

Visit:  https://www.codewars.com/kata/5672682212c8ecf83e000050

Consider a sequence u where u is defined as follows:

<li>
The number <kbd>u(0) = 1</kbd> is the first one in <kbd>u</kbd>.
For each <kbd>x</kbd> in <kbd>u</kbd>, then <kbd>y = 2 * x + 1</kbd> and <kbd>z = 3 * x + 1</kbd> must be in <kbd>u</kbd> too.
There are no other numbers in <kbd>u</kbd>.
</li>
Ex: <kbd>u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]</kbd>

1 gives 3 and 4, then 3 gives 7 and 10, 4 gives 9 and 13, then 7 gives 15 and 22 and so on...

Task:
Given parameter <kbd>n</kbd> the function <kbd>dbl_linear</kbd> (or dblLinear...) returns the element <kbd>u(n)</kbd> of the ordered (with <) sequence <kbd>u</kbd> (so, there are no duplicates).

Example:
<kbd>dbl_linear(10)</kbd> should return 22

Note:
Focus attention on efficiency
