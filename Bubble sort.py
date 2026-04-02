
#Bubble sorting:
1.1
def leaderboard(arr):
    n=len(arr)
    swap_count = 0
    for i in range(n-1):
        for j in range(0,n-1-i):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swap_count+= 1
    return arr,swap_count
arr = [300,150,400,250,100]
leaderboards, total_swaps = leaderboard(arr)
print(f"scores:{leaderboards}")  
print(f"rank changes:{total_swaps}")

1.2
def leaderboard_score(player_score):
    n = len(player_score)
    rank_changes = 0
    for i in range(n-1):
        for j in range(0,n-1-i):
            if player_score[j]<player_score[j+1]:
                player_score[j],player_score[j+1] = player_score[j+1],player_score[j]
                rank_changes+= 1
    return player_score, rank_changes
player_score =[500,100,400,200,300]
leaderboard,total_swaps = leaderboard_score(player_score)
print(f"leaderboard:{leaderboard}")
print(f"rank changes:{total_swaps}")

2.1
def student_grades(arr):
    n=len(arr)
    swaps = 0
    for i in range(n-1):
        for j in range(0,n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swaps +=1
    return arr,swaps
arr = [78,55,92,40,88]
grades,total_swaps = student_grades(arr)
print(f"grades:{grades}") 
print(f"swaps:{total_swaps}") 

2.2
def student_grades(grades):
    n=len(grades)
    swaps = 0
    for i in range(n-1):
        for j in range(0,n-1-i):
            if grades[j]>grades[j+1]:
                grades[j],grades[j+1]
                swaps+=1
    return grades,swaps
grades= [90,85,80,75,70]
grades,total_swaps = student_grades(grades)
print(f"sorted:{grades}")
print(f"swaps:{total_swaps}")            

