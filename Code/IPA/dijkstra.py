from fibonacci_heap_mod import Fibonacci_heap as fh

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

def dijkstra(vertex, whole_set, distances):
    entries = {}
    prev = {}
    Q = fh()
    entries[vertex] = Q.enqueue(vertex, 0)
    while len(Q) > 0:
        min_vertex_entry = Q.dequeue_min()
        neighbour_distances = neighbours(min_vertex_entry.get_value(), whole_set, distances)
        for neighbour in neighbour_distances:
            alt = min_vertex_entry.get_priority() + neighbour_distances[neighbour]
            if neighbour not in entries or alt < entries[neighbour].get_priority():
                if neighbour in entries:
                    Q.decrease_key(entries[neighbour], alt)
                else:
                    entries[neighbour] = Q.enqueue(neighbour, alt)
                prev[neighbour] = min_vertex_entry.get_value()
    dist = {key: entries[key].get_priority() for key in entries}
    return dist, prev
