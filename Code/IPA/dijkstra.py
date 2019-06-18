def neighbours(vertex, whole_set, distances):
    ns = {}
    if vertex == 'X':
        vertex = ()
    for elem in vertex:
        tup = tuple(e for e in vertex if e != elem)
        if len(tup) == 0:
            tup = 'X'
        if ('X', elem) in distances:
            ns[tup] = distances[('X', elem)]
        for other_elem in whole_set - set(vertex):
            if (other_elem, elem) in distances:
                dist = distances[(other_elem, elem)]
                ns[tuple(sorted([other_elem if e == elem else e for e in vertex]))] = dist
    for other_elem in whole_set - set(vertex):
        if (other_elem, 'X') in distances:
            ns[tuple(sorted(list(vertex + (other_elem,))))] = distances[(other_elem, 'X')]
    return ns

def pop_minimal_vertex(Q, dist):
    mv = None
    md = None
    for v in Q:
        if md is None or md > dist[v]:
            mv, md = v, dist[v]
    Q.remove(mv)
    return mv

def dijkstra(vertex, whole_set, distances):
    dist = {}
    prev = {}
    dist[vertex] = 0
    Q = {vertex}
    while len(Q) > 0:
        min_vertex = pop_minimal_vertex(Q, dist)
        neighbour_distances = neighbours(min_vertex, whole_set, distances)
        for neighbour in neighbour_distances:
            alt = dist[min_vertex] + neighbour_distances[neighbour]
            if neighbour not in dist or alt < dist[neighbour]:
                dist[neighbour] = alt
                prev[neighbour] = min_vertex
                Q.add(neighbour)
    return dist, prev
