from collections import defaultdict
from heapq import *

def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))

    q, seen = [(0,f,())], set()
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t: return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 not in seen:
                    heappush(q, (cost+c, v2, path))

    return float("inf")

if __name__ == "__main__":
    edges = [
        ("A", "B", 4),
        ("A", "C", 3),
        ("A", "E", 7),
        ("B", "A", 4),
        ("B", "C", 6),
        ("B", "L", 5),
        ("C", "A", 3),
        ("C", "B", 6),
        ("C", "D", 11),
        ("D", "C", 11),
        ("D", "F", 6),
        ("D", "L", 9),
        ("D", "G", 10),
        ("E", "A", 7),
        ("E", "G", 5),
        ("F", "D", 6),
        ("F", "L", 5),
        ("G", "E", 5),
        ("G", "D", 10),
        ("L", "B", 5),
        ("L", "D", 9),
        ("L", "F", 5)
    ]

    print("=== Dijkstra ===")
    print(edges)
    print("A -> F:")
    print(dijkstra(edges, "A", "F"))
    print("A -> E:")
    print(dijkstra(edges, "A", "E"))