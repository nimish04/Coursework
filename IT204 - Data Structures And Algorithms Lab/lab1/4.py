import time
def selection_sort(array):
	for i in range(len(array) - 1):
		pos = i
		smallest = array[pos]
		for j in range(i + 1, len(array)):
			if array[j] < smallest:
				pos = j
				smallest = array[pos]
		array[i], array[pos] = array[pos], array[i]
	return array

def bubble_sort(array):
	for i in range(len(array)):
		for j in range(len(array) - i - 1):
			if array[j] > array[j + 1]:
				array[j], array[j + 1] = array[j + 1], array[j]
	return array

n = int(input("Enter number of elements: "))
arr = []
for a in range(n):
	new_element = input("Enter element" + str(a + 1) + ": ")
	arr.append(new_element)
print("Selection sort: ")
start1 = time.time()
print(selection_sort(arr))
print(time.time() - start1)
print("Bubble sort: ")
start2 = time.time()
print(bubble_sort(arr))
print(time.time() - start2)