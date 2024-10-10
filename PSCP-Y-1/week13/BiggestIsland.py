"""BiggestIsland"""
def dfs(matrix, visited, i, j, m, n):
    """BiggestIsland"""
    directions = [(-1, -1), (-1, 0), (-1, 1),\
    (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    visited[i][j] = True
    size = 1
    for d in directions:
        new_i, new_j = i + d[0], j + d[1]
        if 0 <= new_i < m and 0 <= new_j < n \
        and not visited[new_i][new_j] and matrix[new_i][new_j] == 1:
            size += dfs(matrix, visited, new_i, new_j, m, n)
    return size
def largest_island(matrix, m, n):
    """BiggestIsland"""
    visited = [[False for _ in range(n)] for _ in range(m)]
    max_size = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1 and not visited[i][j]:
                island_size = dfs(matrix, visited, i, j, m, n)
                max_size = max(max_size, island_size)
    return max_size
def main():
    """BiggestIsland"""
    m, n = map(int, input().strip().split())
    matrix = []
    for _ in range(m):
        row = list(map(int, input().strip().split()))
        matrix.append(row)
    result = largest_island(matrix, m, n)
    print(result)
main()
