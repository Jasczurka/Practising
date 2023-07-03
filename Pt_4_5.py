def func(root, way=""):
    global graph, res, end
    way += root
    if root == end:
        res.append(way)
        return None
    for el in graph[root]:
        func(el, way)


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start = "A"
end = "F"
res = []
func(start)
print(*["-".join(list(el)) for el in res], sep="\n")
