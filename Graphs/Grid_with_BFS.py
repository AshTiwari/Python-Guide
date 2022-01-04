# Shortest Path in a Grid.

def addAdjacentNodes(node):
    dir_row = [0, 0, -1, +1]
    dir_col = [-1, +1, 0, 0]
    r,c = node[0], node[1]

    adjacent_nodes = []
    for delta_r, delta_c in zip(dir_row, dir_col):
        adjacent_nodes.append((r+delta_r, c+delta_c))
    return adjacent_nodes

def gridShortestDistance(grid, start, R, C):
    if grid[start[0]][start[1]] == "E":
        return 0
    global total_rows, total_columns
    total_rows, total_columns = R, C
    visited = [[0 for i in range(C)] for i in range(R)]
    visited[0][0] = 1
    current_level_nodes = []
    current_level_nodes.append((start[0],start[1]))
    next_level_nodes = []
    current_level = 1
    found = False
    while(current_level_nodes):
        for current_node in current_level_nodes:
            adjacent_nodes = addAdjacentNodes(current_node)
            for child_node in adjacent_nodes:
                r, c = child_node[0], child_node[1]
                if r < 0 or r >= R: continue
                if c < 0 or c >= C: continue
                if grid[r][c] == -1: continue
                if grid[r][c] == "E":
                    found = True
                    break
                if visited[r][c] == 0:
                    visited[r][c] = 1
                    next_level_nodes.append((r,c))
        if found == True:
            break
        current_level_nodes = [node for node in next_level_nodes]
        next_level_nodes = []
        current_level += 1
    return -1 if found == False else current_level

def gridShortestPath(grid, start, R, C):
    if grid[start[0]][start[1]] == "E":
        return 0,[(0,0)]
    global total_rows, total_columns
    total_rows, total_columns = R, C
    visited = [[0 for i in range(C)] for i in range(R)]
    visited[0][0] = None
    current_level_nodes = []
    current_level_nodes.append((start[0],start[1]))
    next_level_nodes = []
    current_level = 1
    found = False
    while(current_level_nodes):
        for current_node in current_level_nodes:
            adjacent_nodes = addAdjacentNodes(current_node)
            for child_node in adjacent_nodes:
                r, c = child_node[0], child_node[1]
                if r < 0 or r >= R: continue
                if c < 0 or c >= C: continue
                if grid[r][c] == -1: continue
                if grid[r][c] == "E":
                    visited[r][c] = current_node
                    found = True
                    break
                if visited[r][c] == 0:
                    visited[r][c] = current_node
                    next_level_nodes.append((r,c))
        if found == True:
            break
        current_level_nodes = [node for node in next_level_nodes]
        next_level_nodes = []
        current_level += 1
    
    if found == False:
        return -1
    else:
        path = [(r,c)]
        while((r,c) != start):
            path.append(visited[r][c])
            r, c = visited[r][c][0], visited[r][c][1]
        path.reverse()
        return current_level, path    

if __name__ == "__main__":
    grid = [['S',0,0,-1,0,0,0],[0,-1,0,0,0,-1,0],[0,-1,0,0,0,0,0],[0,0,-1,-1,0,0,0],[-1,0,-1,'E',0,-1,0]]
    start = (0,0)
    print(gridShortestDistance(grid, start,5,7))
    print(gridShortestPath(grid, start,5,7))
