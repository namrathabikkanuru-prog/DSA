#insertion sorting:
1.
def insertion_sort(scores):
    n=len(scores)
    shifts = 0
    for i in range (1,n):
        key = scores[i]
        j = i-1
        while j>=0 and scores[j] > key:
            shifts += 1
            scores[j+1]= scores[j]   
            j = j-1
            scores[j+1] = key
    return scores,shifts
scores = [72,45,88,60,95]
# scores1 =[10,20,30,40,50]
print(insertion_sort(scores)) 

2.
def sort_books(pages):
    n = len(pages)
    shifts = 0
    for i in range(1,n):
        Key = pages[i]
        j = i-1
        while j>=0 and pages[j] >Key :
            shifts+= 1
            pages[j+1]= pages[j]
            j = j-1
            pages[j+1]= Key
    return pages,shifts        
pages = [300,150,400,250,100]
pages1 = [500,100,400,250,100]
print(sort_books(pages)) 
print(sort_books(pages1))    
