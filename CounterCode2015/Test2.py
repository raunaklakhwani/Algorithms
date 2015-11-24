from collections import deque
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        def bfs(board, x, y, visited, adj):
            visited[i][j] = True
            q = deque([(i, j)])
            res = [(i, j)]
            
            while len(q):
                x, y = q.popleft()
                for a, b in adj:
                    nx = x + a
                    ny = y + b
                    if nx >= 0 and nx < len(board) and ny >= 0 and ny < len(board[0]) and not visited[nx][ny]:
                        if board[nx][ny] == "O":
                            visited[nx][ny] = True
                            res.append((nx, ny))
                            q.append((nx, ny))
                    elif not (nx >= 0 and nx < len(board) and ny >= 0 and ny < len(board[0])):
                        return
            else:
                for a, b in res:
                    board[a][b] = "X"
                
                    
            
            
        
        
        
        visited = [[False] * len(board[0]) for _ in xrange(len(board))]
        
        for i in xrange(len(board)):
            board[i] = list(board[i])
            
            
        adj = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if not visited[i][j] and board[i][j] == "O":
                    bfs(board, i, j, visited, adj)
                    
                    
        for i in xrange(len(board)):
            board[i] = "".join(board[i])
        
        print board
                
                
if __name__ == '__main__':
    s = Solution()
    s.solve(["OXOOOOOOO","OOOXOOOOX","OXOXOOOOX","OOOOXOOOO","XOOOOOOOX","XXOOXOXOX","OOOXOOOOO","OOOXOOOOO","OOOOOXXOO"])
    
    
