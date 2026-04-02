
# merge sort :

# 912

def merge_sort(arr):
    if len (arr)<1:
        return arr
    if len(arr)>1:
        mid = len(arr)//2
        L= arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j= k = 0
        while i<len(L) and j<len(R):
            if L[i]< R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j +=1
            k+=1
        while i<len(L):
            arr[k] = L[i]
            i+=1
            k+=1
        while j<len(R):
            arr[k] = R[j]
            j+=1
            k+=1
    return arr
# arr = [5,2,3,1]
arr = [5,1,1,2,0,0]
print(merge_sort(arr))


# 287 find the duplicate

def merge_sort(arr):
    if len(arr) <= 1:
        return arr    #return the sorted list
    
    mid = len(arr)// 2
    left = merge_sort (arr[:mid])
    right = merge_sort (arr[:mid])

    merge_sort(left)
    merge_sort(right)

    i=j=k= 0

    while i < len(left) and j< len(right):
        if left[i] < right[i]:
            arr [k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i< len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j< len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return arr

def find_duplicates(arr):
    dup = []
    for i in range (1, len(arr)):
        if arr[i]== arr[i-1] and arr[i] not in dup :
            dup.append(arr[i])
    return dup

arr = [5,2,3,13,1,2,13,5,4]  
merge_sort(arr)
duplicates = find_duplicates(arr)

print("sorted:", arr)
print("duplicates:", duplicates)
            