# counting sort.

def countingSortPythonic(array, biggestElement):
    count = [0 for i in range(biggestElement + 1)]
    for i in array:
        count[i] += 1
    sorted_array = []
    for element,freq in enumerate(count):
        for j in range(freq):
            sorted_array.append(element)
            
    return sorted_array
        
def counting_sort(input_array, biggestElement):   
    count = [0 for i in range(biggestElement + 1)]
    for i in input_array:
        count[i] +=1

    for i in range(biggestElement + 1):
        count[i] += count[i-1]

    sorted_array = [0 for i in range(len(input_array))]
    for i in input_array:
        index = count[i]
        count[i] -=1
        sorted_array[index-1] = i

    return sorted_array

if __name__ == "__main__":
    print('Enter the space seperated array.')
    input_array = list(map(int,input().split()))
    print(counting_sort(input_array,9))
    print(countingSortPythonic(input_array, 9))
