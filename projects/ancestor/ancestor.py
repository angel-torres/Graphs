
def earliest_ancestor(ancestors, starting_node):
    ancestor_verts = {}
    # add all pairs into a dictionary
    for pair in ancestors:
        if pair[0] not in ancestor_verts:
            ancestor_verts[pair[0]] = set()
            ancestor_verts[pair[0]].add(pair[1]) 
        else:
            ancestor_verts[pair[0]].add(pair[1]) 

    if starting_node not in ancestor_verts:
        return -1
    
    # initialize stack for dft
    stack = []

    # pop starting node
    stack.append(starting_node)
    visited = set()
    while len(stack) > 0:
        # pop the first vertex
        vert = stack.pop()
        if len(stack) == 1:
            return vert
        # If that vertex has not been visited...
        if vert not in visited:
            # Mark it as visited
            visited.add(vert)
            # Add all of its neighbors to the back of the stack          
            for v in ancestor_verts[vert]:
                stack.append(v)


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

earliest_ancestor(test_ancestors, 5)