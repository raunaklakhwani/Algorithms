'''
4 4
-1 4 5 1
2 -1 2 4
3 3 -1 3
4 2 1 2

4 4
-1 4 5 1
2 -1 2 4
3 3 -1 -1
4 2 1 2
'''

def dfs(grid, r, c, s, visited):
    global m
    print r,c,s
    # visited[r][c] = True
    for a, b in adj:
        x = r + a
        y = c + b
        if y == len(grid[0]):
            m = max(m,s)
        elif x < 0:
            x = len(grid) - 1
            if grid[x][y] != -1 and not visited[x][y]:
                visited[x][y] = True
                dfs(grid, x, y, grid[x][y], visited)
                visited[x][y] = False
        elif x == len(grid):
            x = 0
            if grid[x][y] != -1 and not visited[x][y]:
                visited[x][y] = True
                dfs(grid, x, y, grid[x][y], visited)
                visited[x][y] = False
        elif x >= 0 and x < len(grid):
            if grid[x][y] != -1 and not visited[x][y]:
                visited[x][y] = True
                dfs(grid, x, y, s + grid[x][y], visited)
                visited[x][y] = False
        
            


R, C = map(int, raw_input().split())
grid = []

for _ in xrange(R):
    grid.append(map(int, raw_input().split()))
    
adj = [(1, 0), (-1, 0), (0, 1)]
m = 0

visited = []
for i in xrange(R):
    visited.append([])
    for j in xrange(C):
        visited[i].append(False)


for i in xrange(R):
    if grid[i][0] != -1:
        visited[i][0] = True
        dfs(grid, i, 0, grid[i][0], visited)
        visited[i][0] = False
        
print m
    


                
                
