def recurse_fib(n):
	if n in store:
		return store[n]
	else:
		f = recurse_fib(n - 1) + recurse_fib(n - 2)
	store[n] = f
	return f
def iter_fib(n):
	print(1)
	print(1)
	first = 1
	second = 1
	third = first + second
	for i in range(n - 2):
		third = first + second
		print(third)
		first, second = second, third

global store
store = {1: 1, 2: 1}
num = int(input("Enter number of fibonacci numbers you want to output: "))
print("Fib using iteration:")
iter_fib(num)
print("Fib using recursion:")
for i in range(1, num + 1):
	print(recurse_fib(i))