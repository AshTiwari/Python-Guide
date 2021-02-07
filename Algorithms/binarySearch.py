# Find element in an sorted array.

def binarySearch(array, element, mode = 0):
	n = len(array)
	left, right = 0, n-1
	mid = (left+right)//2
	found = 0	
	while(left <= right):		
		if array[mid] == element:			
			found = 1
			break
		elif array[mid] > element:
			right = mid - 1
			mid = (left+right)//2
		elif array[mid] < element:
			left = mid + 1
			mid = (left+right)//2

	if mode == 0:
		return mid if found == 1 else -1

	else:
		least_index = mid 
		while(least_index > -1 and array[least_index] == element ):
			least_index -= 1
		least_index += 1
		if mode == 1: 
			return least_index if found == 1 else -1 
		elif mode == 2:
			return least_index if found == 1 else (left, right, n)
		elif mode == 3:
			frequency, index = 0, least_index
			while(index < n and array[index] == element ):
				frequency += 1 
				index += 1
			return (least_index, frequency) if found == 1 else (-1, frequency)



def firstInstanceBinarySearch(array, element):
	return binarySearch(array, element, 1)

def BinarySearchWithFrequency(array, element):
	return binarySearch(array, element, 3)

def lessThanEqualBinarySearch(array, element):
	input =  binarySearch(array,element, 2)
	if isinstance(input, int):
		return input
	elif isinstance(input, tuple):
		left, right, n = input
		return right

def GreaterThanEqualBinarySearch(array, element):
	input =  binarySearch(array,element, 2)
	if isinstance(input, int):
		return input 
	elif isinstance(input, tuple):
		left, right, n = input
		return left if left < n else -1


if __name__ == "__main__":
	array = [0, 1, 2, 3, 5, 5, 5, 5, 7, 8, 9]
	#array = [1]
	element = 4
	print(binarySearch(array,element))
	print(firstInstanceBinarySearch(array,element))
	print(BinarySearchWithFrequency(array,element))
	print(lessThanEqualBinarySearch(array,element))
	print(GreaterThanEqualBinarySearch(array,element))
	