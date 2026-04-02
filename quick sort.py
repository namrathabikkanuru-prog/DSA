

# quick sort
1.
def quick_sort(number_of_pages):
    if len(number_of_pages)<= 1:
        return number_of_pages
    else:
        pivot = number_of_pages[len(number_of_pages)// 2]
        left = [x for x in number_of_pages if x < pivot]
        right = [x for x in number_of_pages if x > pivot]
        mid = [x for x in number_of_pages if x == pivot]
        return quick_sort(left)+mid +quick_sort(right)
number_of_pages =[400,50,300,200]
print(quick_sort(number_of_pages))  

2.

def quick_sort(players):
    if len(players) <= 1:
        return players
    else:
        pivot = players[len(players)//2] [1]
        left = [x for x in players if x[1] > pivot]
        right = [x for x in players if x [1]< pivot]
        mid = [x for x in players if x[1] == pivot]
        return quick_sort(left)+ mid + quick_sort(right)

players =[("rohit",85),("virat",120),("dhoni",60),("hardik",95),("rahul",110)]
print(quick_sort(players))


# ANOTHER FORM 
def quick_sort(arr):
    n= len(arr)
    if n<=1:
        return arr
    pivot = arr[0]
    left = []
    right = []
    for i in range (1,n):
        if arr [i][1]>= pivot[1]:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return  quick_sort(left)+[pivot]+quick_sort(right )

arr = [("rohit", 85),("virat",120),("dhoni",60),("hardik",95),("rahul",110)] 
print("players=",quick_sort(arr)) 