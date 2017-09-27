def iter_fact(n):
	toret = 1
	for i in range(2, n + 1):
		toret *= i
	return toret

def recurse_fact(n):
	if (n == 1):
		return n
	else:
		return (n * recurse_fact(n - 1))

a = int(input("Enter a number: "))
print("Factorial by iterating: " + str(iter_fact(a)))
print("Factorial by recursion: " + str(recurse_fact(a)))