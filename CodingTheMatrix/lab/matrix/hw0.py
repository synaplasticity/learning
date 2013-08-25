# Please fill out this stencil and submit using the provided submission script.





## Problem 1
def myFilter(L, num):
	"""
	input: list of numbers and a number.
	output: list of numbers not containing a multiple of num.
	example: given list = [1,2,4,5,7] and num = 2, return [1,5,7].
	"""
	print ('List : ' + str(L))
	print ('Number : ' + str(num))
	return [number for number in L if number%num != 0]

## Problem 2
def myLists(L):
	"""
	nput: list L of non-negative integers.
	output: a list of lists: for every element x in L create a list containing 1,2,...,x.
	example: given [1,2,4] return [[1],[1,2],[1,2,3,4]].
	"""

	return [list(range(1, number+1)) for number in L]



## Problem 3
def myFunctionComposition(f, g):
	"""
	input: two functions f and g, represented as dictionaries, such that g ◦ f exists.
	output: dictionary that represents a function g ◦ f.
	example: given f = {0:’a’,1:’b’} and g = {’a’:’apple’,’b’:’banana’}, return {0:’apple’,1:’banana’}.
	"""
	return {key:g[ f[key] ] for key in f.keys()}


## Problem 4
# Please only enter your numerical solution.

complex_addition_a = (5+3j)
complex_addition_b = 1j
complex_addition_c = (-1+0.001j)
complex_addition_d = (0.001+9j) 




## Problem 5
GF2_sum_1 = 1
GF2_sum_2 = 0
GF2_sum_3 = 0


## Problem 6
def mySum(L):
	current = 0
	for x in L:
		current += x

	return current



## Problem 7
def myProduct(L):
	current = ''
	for x in L:
		if current == '':
			current = x
		else:
			current *= x

	return current	



## Problem 8
def myMin(L):
	min = ''

	for x in L:
		if min == '':
			min = x
		else:
			if (x < min):
				min = x

	return min



## Problem 9
	current_string = ''
	for string in L:
		if current_string == '':
			current_string = string
		else:
			current_string += string

	return current_string



## Problem 10
def myUnion(L):
	set_union = set()

	for s in L:
		if set_union == set():
			set_union = s
		else:
			set_union.update(s)

	return set_union


"""
In each of the above problems, the value of current is combined with an element of myList using some
operation ?. In order that the procedure return the correct result, current should be initialized with the
identity element for the operation ?, i.e. the value i such that i ? x = x for any value x.
It is a consequence of the structure of the procedure that, when the input list is empty, the output value
is the initial value of current (since in this case the body of the loop is never executed). It is convenient to
define this to be the correct output!
"""