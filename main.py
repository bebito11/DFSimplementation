def DFS(G, S, visited):
    """function that verifies the visited vertices"""
    num = int(S) - 1
    for n in G[num]:  # n =  elements of the line G[num]
        if len(G[num]) == 1 and (n not in visited):
            """verifies if G[num] has only one element and if n is not yet visited"""
            visited.append(n)
            break
        elif len(G[num]) == 1:
            """verifies only if G[num] has one element"""
            break
        if n not in visited:
            """verifies if n is not yet visited and appends it to the stack"""
            visited.append(n)
            visited.append(DFS(G, n, visited))

    return visited


def DFSloop(G, visited):
    """trate de implementar esta funcion y no me salio"""
    visited = []
    currentLabel = len(G)
    for vertex in G:
        if vertex not in visited:
            visited.append(DFS(G, vertex, visited))

    return visited


graph = []  # array to hold file contents
graphTxt = input("File name: ")
startingPosition = input("Vertex starting position: ")
"""read file and make sub arrays of each line"""
with open(graphTxt, "r") as f:
    for line in f:  # reads file line by line
        graph.append(line.split())


visited = []
visited.append(DFS(graph, startingPosition, visited))
print(visited)
