"""Island"""
def dfs(matrix, visited, i, j, m, n):
    """Island"""
    directions = [(-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    visited[i][j] = True
    for d in directions:
        new_i, new_j = i + d[0], j + d[1]
        if 0 <= new_i < m and 0 <= new_j < n \
        and not visited[new_i][new_j] and matrix[new_i][new_j] == 1:
            dfs(matrix, visited, new_i, new_j, m, n)
def count_islands(matrix, m, n):
    """Island"""
    visited = [[False for _ in range(n)] for _ in range(m)]
    island_count = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1 and not visited[i][j]:
                dfs(matrix, visited, i, j, m, n)
                island_count += 1
    return island_count
def main():
    """Island"""
    m, n = map(int, input().strip().split())
    matrix = []
    for _ in range(m):
        row = list(map(int, input().strip().split()))
        matrix.append(row)
    result = count_islands(matrix, m, n)
    print(result)
main()
