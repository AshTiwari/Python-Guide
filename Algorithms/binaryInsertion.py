# Insert an element in sorted array.

def binaryInsertion(arr, element):
    n = len(arr)
    arr.append(None)
    left = 0
    right = n-1
    mid = (left+right)//2
    position = None
    while(position == None):
        if element <= arr[left]:
            position = left
        elif arr[right] <= element:
            position = right + 1
        elif element == arr[mid]:
            position = mid + 1
        elif element < arr[mid]:
            right = mid-1
            mid = (left+right)//2
        elif element > arr[mid]:
            left = mid + 1
            mid = (left+right)//2
    shift_index = n
    while(shift_index > position):
        arr[shift_index] = arr[shift_index-1]
        shift_index -= 1	
    arr[position] = element			
    return arr

if __name__ == "__main__":
    #arr = [0,1,3,5,7,9,15]
    #element = 16
    arr = [1,3,9,11,14,16]
    element = 8
    array = binaryInsertion(arr,element)
    print(*array)

