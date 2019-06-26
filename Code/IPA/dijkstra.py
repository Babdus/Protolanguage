from fibonacci_heap_mod import Fibonacci_heap as fh
from IPA.IPAData import vowels, places, secondary_places, manners, secondary_manners, airflows

def is_valid_sound(tup):
    features = set(tup)
    return (len(features & places) < 2 or (len(features & {'AL', 'PA'}) == 2 and len(features & places) == 2)) and len(features & manners) < 2

def neighbours(vertex, whole_set, distances):
    ns = {}
    if vertex == 'X':
        vertex = ()
    for elem in vertex:
        if ('X', elem) in distances:
            tup = tuple(e for e in vertex if e != elem)
            if len(tup) == 0:
                tup = 'X'
            if is_valid_sound(tup):
                ns[tup] = distances[('X', elem)]
        for other_elem in whole_set - set(vertex):
            if (other_elem, elem) in distances:
                tup = tuple(sorted([other_elem if e == elem else e for e in vertex]))
                if is_valid_sound(tup):
                    ns[tup] = distances[(other_elem, elem)]
    for other_elem in whole_set - set(vertex):
        if (other_elem, 'X') in distances:
            tup = tuple(sorted(list(vertex + (other_elem,))))
            if is_valid_sound(tup):
                ns[tup] = distances[(other_elem, 'X')]
    return ns

def add_intermediate_features(vertex, whole_set):
    features1 = set(vertex)
    features2 = whole_set - features1
    vowel_list = ['CL', 'NC', 'MC', 'MI', 'MO', 'NO', 'OP']
    if len(features1 & vowels) > 0 and len(features2 & vowels) > 0:
        vowel1 = (features1 & vowels).pop()
        vowel2 = (features2 & vowels).pop()
        index1 = vowel_list.index(vowel1)
        index2 = vowel_list.index(vowel2)
        if index1 > index2:
            adding_sublist = vowel_list[index2+1:index1]
        else:
            adding_sublist = vowel_list[index1+1:index2]
        whole_set |= set(adding_sublist)
    return whole_set

def dijkstra(vertex, whole_set, distances):
    whole_set = add_intermediate_features(vertex, whole_set)
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
