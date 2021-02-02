# Merge Sort

def merge(leftArray, rightArray):
	index1 = index2 = 0
	m = len(leftArray)
	n = len(rightArray)
	sortedArray = []	
	while(index1 < m and index2 < n):
		if leftArray[index1] <= rightArray[index2]:
			sortedArray.append(leftArray[index1])
			index1 += 1 
		elif leftArray[index1] >= rightArray[index2]:
			sortedArray.append(rightArray[index2])			
			index2 += 1
	if index1 < m:
		for i in range(index1,m):
			sortedArray.append(leftArray[i])
	elif index2 < n:
		for i in range(index2,n):
			sortedArray.append(rightArray[i])
	return sortedArray

def mergeSort(array):
	if len(array) <= 1:
		return array
	left = 0
	right = len(array)
	mid = (left+right)//2

	leftSubArray = mergeSort(array[left:mid]) 
	rightSubArray = mergeSort(array[mid:right])
	array = merge(leftSubArray,rightSubArray)
	return array

if __name__ == "__main__":
	#array = [2,4,5,8,3,0,15,1]
	#array = [2,4,5,8,3,0,15]
	#array = [0,0,0,0,0,0,0,0,0]
	array = [1]
	print(mergeSort(array))