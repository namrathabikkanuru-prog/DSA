
#graph :

def has_cycle(graph):
    visited = set()

    def dfs (node, parent):
        visited.add(node)

        for neighbour in graph[node]:
            if neighbour not in  visited:
                if dfs(neighbour,node):
                    return True
            elif neighbour != parent:
                return True 
        return False
    for node in graph:
        if node not in visited:
            if dfs(node, -1):
                return True
    return False

graph1  = {
    0: [1,2],
    1: [0,3],
    2: [0,3],
    3: [1,2]
} 

print ("cycle detected" if has_cycle(graph1) else "no cycle found")

graph2 = {
    0: [1],
    1: [0,3],
    2: [1]
}

print ("cycle detected " if has_cycle(graph2) else "no cycle found")