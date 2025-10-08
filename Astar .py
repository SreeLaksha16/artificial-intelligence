from queue import PriorityQueue

def a_star(graph, start, goal, h):
    pq = PriorityQueue()
    pq.put((0, start))
    g = {start: 0}
    parent = {start: None}

    while not pq.empty():
        _, current = pq.get()
        if current == goal:
            break
        for neighbor, cost in graph[current]:
            new_g = g[current] + cost
            if neighbor not in g or new_g < g[neighbor]:
                g[neighbor] = new_g
                f = new_g + h[neighbor]
                pq.put((f, neighbor))
                parent[neighbor] = current

    path = []
    node = goal
    while node:
        path.append(node)
        node = parent[node]
    print("Path:", path[::-1])
    print("Cost:", g[goal])

graph = {
    'A': [('B',1), ('C',3)],
    'B': [('D',3), ('E',1)],
    'C': [('F',5)],
    'D': [('G',2)],
    'E': [('G',1)],
    'F': [('G',2)],
    'G': []
}
h = {'A':6,'B':4,'C':5,'D':2,'E':1,'F':2,'G':0}
a_star(graph,'A','G',h)
