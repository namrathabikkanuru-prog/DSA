
# Dynamic programming :

# fibonacci :

# def fibonacci (n, memo = {}):
#     if n<= 1:
#         return n
#     if n in memo:
#         return memo[n]
    
#     memo[n] = fibonacci(n - 1, memo) + fibonacci(n-2,memo)
#     return memo[n]

# print ("fibonacci(10) =", fibonacci(10))
# print ("fibonacci(30)=", fibonacci(30))




# # knapsack :

# def knapsack(weights,values,capacity):
#     n = len(weights)
#     dp = [[0 for _ in range (capacity+1)] for _ in range (n+1)]

#     for i in range (1,n+1):
#         for w in range (capacity+1):
#             if weights[i-1] <= w:
#                 dp [i][w] = max (dp[i-1][w], values [i-1] + dp [i-1][w-weights[i-1]])

#             else:
#                 dp[i][w] = dp[i-1][w]
        
#     choosen_items = []
#     w = capacity

#     for i in range (n,0,-1):
#         if dp [i][w] != dp[i-1][w]:
#             choosen_items.append(i)
#             w -= weights[i-1]
#         choosen_items. reverse()
#         return dp[n][capacity],choosen_items    
# weights = [1,2,3,5]
# values = [1,6,10,16]
# capacity = 7


# max_value,items = knapsack(weights,values,capacity)
# print("max value:", max_value)
# print("items choosen:",items)

# for item in items :
#     print(f"item {item} : weight = {weights [item-1]}, value = {values[item-1]}")