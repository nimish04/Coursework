def evaluatePostfix(expression):
	S = []
	index = 0
	expression = expression.split(" ")
	while (index < len(expression)):
		ch = expression[index]
		if ch.isdigit():
			S.append(float(ch))
		else:
			try:
				second = float(S.pop())
				first = float(S.pop())
			except:
				return False
			result = 0
			if (ch == '+'):
				result = first + second
			elif (ch == '-'):
				result = first - second
			elif (ch == '*'):
				result = first * second
			elif (ch == '/'):
				result = first / second
			S.append(result)
		index = index + 1
		print(S)
	if len(S) != 1:
		return "Invalid!"
	else:
		return S.pop()

ex = input("Expression: ")
print("Evaluated expression: " + str(evaluatePostfix(ex)))