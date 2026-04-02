
# # binary search : 

def binary_search(arr, target):
    left = 0
    right = len(arr) -1
    while left<=right:
        mid  = left + (right-left)//2
        if arr[mid]== target:
            print("seat",target,"is available !")
            return arr
        elif arr[mid] < target:
            left = mid+1
        else:
            right = mid-1
    print('seat',target,"is not available")
available_seats = [2,5,9,14,21,28,35,42,48,55]
preferred_seat = 28
binary_search(available_seats, preferred_seat)    
