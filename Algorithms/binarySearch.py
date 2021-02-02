# Find element in an sorted array.

def binarySearch(array,element,freq = 0):
	n = len(array)
	left = 0
	right = n-1
	mid = (left+right)//2
	found = 0
	frequency = 0
	
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
	
	if freq != 0 and found ==0:		
		return -1,0
	elif freq != 0 and found == 1:
		i = mid + 1
		while(i < n and array[i] == element ):
			frequency += 1
			i += 1
		least_index = mid 
		while(least_index > -1 and array[least_index] == element ):
			frequency += 1
			least_index -= 1
		return least_index+1, frequency
				
		
		
	return mid if found == 1 else -1

if __name__ == "__main__":
	array = [0, 1, 2, 3, 5, 5, 5, 5, 7, 8, 9]
	#array = [1]
	element = 5
	print(binarySearch(array,element))
	print(binarySearch(array,element,1))