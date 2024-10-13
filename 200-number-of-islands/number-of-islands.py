class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def get_neighbors(grid, row, column):
            d=[(0,1),(1,0),(0,-1),(-1,0)]
            neighbors=[]
            for nei in d:
                new_row=row + int(nei[0])
                new_column=column + int(nei[1])
                #safe neighbors only 
                if 0<=new_row<len(grid) and 0<=new_column<len(grid[0]) and grid[new_row][new_column]=='1':
                    neighbors.append((new_row,new_column))
            
            return neighbors
        
        def dfs(grid,row,column,visited):
            visited.add((row,column))

            for neighbor in get_neighbors(grid,row,column):
                if neighbor not in visited:
                    dfs(grid,neighbor[0],neighbor[1],visited)
        
        visited=set()
        island=0

        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column]=='1' and (row,column) not in visited :
                    dfs(grid,row,column,visited)
                    island=island+1
        
        return island

            
            



        