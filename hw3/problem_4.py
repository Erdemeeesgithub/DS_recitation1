def solver(maze):
    # TODO: Please write your code here
    if not maze or not maze[0]:
        return []
    rows = len(maze)
    cols = len(maze[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    path = []
    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        if maze[r][c] == 0 or visited[r][c]:
            return False
        path.append((r, c))
        visited[r][c] = True
        if r == rows - 1 and c == cols - 1:
            return True
        if dfs(r + 1, c):  
            return True
        if dfs(r, c + 1):  
            return True
        if dfs(r - 1, c):  
            return True
        if dfs(r, c - 1):  
            return True
        path.pop()
        return False

    if dfs(0, 0):
        return path
    else:
        return []


def main():
    res = solver([[1, 0, 1, 1, 1],
                  [1, 0, 1, 0, 1],
                  [1, 0, 1, 0, 1],
                  [1, 1, 1, 0, 1]])

    print(res)  # Should print
    # [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (2, 2), (1, 2), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4)]

    res = solver([[1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                  [0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1],
                  [1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1],
                  [1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
                  [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
                  [1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
                  [1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
                  [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])

    print(res)  # Should print
    # [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (5, 3), (5, 4), (4, 4), (3, 4), (2, 4), (1, 4),
    # (0, 4), (0, 5), (0, 6), (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (4, 8), (4, 9), (4, 10), (3, 10), (2, 10),
    # (2, 11), (2, 12), (3, 12), (4, 12), (5, 12), (6, 12), (7, 12), (8, 12), (9, 12), (9, 13), (9, 14)]


if __name__ == '__main__':
    main()
