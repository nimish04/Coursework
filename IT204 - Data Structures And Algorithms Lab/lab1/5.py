def my_replace(str1, str2, str3):
	newstring = ""
	start = 0
	while start < len(str1):
		if str1[start:start + len(str2)] == str2:
			newstring += str3
			start += len(str2) - 1
		else:
			newstring += str1[start]
		start += 1
	return newstring

first = input("Enter the original string: ")
second = input("Enter the string you want replaced: ")
third = input("Enter the string you want it to be replaced with: ")
print(my_replace(first, second, third))