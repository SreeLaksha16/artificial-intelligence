import itertools

def tsp(graph, start=0):
    n = len(graph)
    vertices = list(range(n))
    vertices.remove(start)

    min_path = float("inf")
    best_route = None

    for perm in itertools.permutations(vertices):
        cost = 0
        k = start
        for j in perm:
            cost += graph[k][j]
            k = j
        cost += graph[k][start]
        if cost < min_path:
            min_path = cost
            best_route = (start,) + perm + (start,)

    print("Best route:", best_route)
    print("Minimum cost:", min_path)

graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
tsp(graph)
