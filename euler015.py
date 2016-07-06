import time
start=time.time()

grid = [[0]*21]*21

#right and bottom row all have 1 path to end
for i in range(0,20):
    grid[i][20] = 1
    grid[20][i] = 1
    
for i in range(19,-1,-1):
    for j in range(19,-1,-1):
        grid[i][j] = grid[i+1][j]+grid[i][j+1]
        
print(grid[0][0])

end=time.time()
print(str(round(end-start,3))+" seconds")
