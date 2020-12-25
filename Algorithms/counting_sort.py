# counting sort.

def counting_sort():   
    count = [0 for i in range(10)]
    for i in input_array:
        count[i] +=1
    #print(count)

    for i in range(1,10):
        count[i] += count[i-1]
    #print(count)

    sorted_array = [0 for i in range(len(input_array))]
    for i in input_array:
        index = count[i]
        count[i] -=1
        sorted_array[index-1] = i
    print(sorted_array)


print('Enter the space seperated array.')
input_array = list(map(int,input().split()))
#print(input_array)
