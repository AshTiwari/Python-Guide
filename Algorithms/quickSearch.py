# implement quick search

# return the element at kth index if the array would had been sorted ascendingly.
def quickSearch(array,start,end,k):
	#print("start")
	pivot = start
	pivotValue = array[start]
	i = start + 1			# moves until it find an element greater than pivotValue. 
	j = end				# moves until it find an element smaller than pivotValue.

	while(1):
		#print(i,j)
		#print(array)
		while(i < end and array[i] < array[pivot]):
			i = i+1
		while(j > start and array[j] >= array[pivot]):
			j = j-1
		if i < j:
			array[i], array[j] = array[j], array[i]
			#print(array)
		elif i >= j:
			array[pivot], array[j] = array[j], array[pivot]
			#print(array)
			break
		
		
	pivot = j
	#print(array)
	#print(pivot)
	if pivot == k:
		result = array[k]
	elif pivot < k:
		result = quickSearch(array,pivot+1,end,k)
	elif pivot > k:
		result = quickSearch(array,start,pivot-1,k)	

	return result

def KthLargest(array,start,end,k):
	return	quickSearch(array,start,end,n-k)

def KthSmallest(array,start,end,k):
	return	quickSearch(array,start,end,k-1)

if __name__ == "__main__":
	#	array = [3,52,66,3,64,28,9,44,70,3,72,1,0]
	array = [3,52,66,64,28,9,44,70,72,1,0]
	n = len(array)
	for i in range(n):	
		k = 0
		while (k < 1 or k > n):
			print("Enter the value of k.")
			k = int(input())
		print(KthLargest(array,0,n-1,k))
		print(KthSmallest(array,0,n-1,k))