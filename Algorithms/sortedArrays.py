# Intersection of sorted Array.

def Union(sorted_array_1,sorted_array_2):
	i = 0				# tracks array 1
	j = 0				# tracks array 2
	array = []
	while(i < len(sorted_array_1) and j < len(sorted_array_2)):
		if sorted_array_1[i] < sorted_array_2[j]:
			if len(array) == 0 or sorted_array_1[i] != array[-1]:
				array.append(sorted_array_1[i])
			i = i+1
		elif sorted_array_1[i] > sorted_array_2[j]:
			if len(array) == 0 or sorted_array_2[j] != array[-1]:
				array.append(sorted_array_2[j])
			j = j + 1
		elif sorted_array_1[i] == sorted_array_2[j]:
			if len(array) == 0 or sorted_array_1[i] != array[-1]:
				array.append(sorted_array_1[i])
			i = i+1
			j = j + 1
	if i == len(sorted_array_1) :
		array.extend(sorted_array_2[j:]) 
	elif j == len(sorted_array_2) :
		array.extend(sorted_array_1[i:]) 

	return array

def Intersection(sorted_array_1,sorted_array_2):
	i = 0				# tracks array 1
	j = 0				# tracks array 2
	array = []
	while(i < len(sorted_array_1) and j < len(sorted_array_2)):
		if sorted_array_1[i] == sorted_array_2[j]:
			if len(array) == 0 or sorted_array_1[i] != array[-1]:
				array.append(sorted_array_1[i])
			i = i+1
			j = j + 1
	
		elif sorted_array_1[i] < sorted_array_2[j]:
			i = i+1
		elif sorted_array_1[i] > sorted_array_2[j]:
			j = j + 1
	return array

def unionK(arrays):
	n = len(arrays)
	if n <= 1:
		return arrays[0]
	elif n == 2:
		return Union(arrays[0],arrays[1])
	else:
		mid = n//2	
		leftSubArray = unionK(arrays[:mid])
		rightSubArray = unionK(arrays[mid:])
		return Union(leftSubArray, rightSubArray)

def intersectionK(arrays):
	n = len(arrays)
	if n <= 1:
		return arrays[0]
	elif n == 2:
		return Intersection(arrays[0],arrays[1])
	else:
		mid = n//2	
		leftSubArray = intersectionK(arrays[:mid])
		rightSubArray = intersectionK(arrays[mid:])
		return Intersection(leftSubArray, rightSubArray)

if __name__ == "__main__":
	sorted_array_0 = [1,2,3,4,5,6,7]
	sorted_array_1 = [1,1,3,5,7]
	sorted_array_2 = [0,1,1,2,4,6,7]
	sorted_array_3 = [1,7]
	#print(Union(sorted_array_1,sorted_array_2))
	#print(Intersection(sorted_array_1,sorted_array_2))
	print(unionK((sorted_array_0,sorted_array_1,sorted_array_2,sorted_array_3)))
	print(intersectionK((sorted_array_0,sorted_array_1,sorted_array_2,sorted_array_3)))
