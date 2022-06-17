# Modify Board 
board = [
    [0,0,0,0,1,8,0,0,0],
    [0,7,0,5,0,0,0,0,0],
    [3,0,0,4,0,0,5,6,0],
    [0,2,4,0,0,0,0,0,9],
    [0,8,0,3,0,6,0,1,0],
    [1,0,0,0,0,0,6,5,0],
    [0,5,2,0,0,9,0,0,8],
    [0,0,0,0,0,1,0,9,0],
    [0,0,0,7,4,0,0,0,0]
]

def solve(bo): 
  find = find_empty(bo)
  # If it can't find an empty space, it stops the function. The 'solve' function will only return 'True' when the sudoku has been solved.
  if not find: return True 
  # Retrieves the row and column of the empty space.
  else: row, col = find 
  
  for i in range (1,10): # 'i'  
    if valid(bo, i, (row, col)):  
      bo[row][col] = i 
      if solve(bo): 
      return True 
      bo[row][col] = 0  
  return False


def valid(bo, num, pos): 
  # Check row. 
  for i in range(len(bo[0])): 
    if bo[pos[0]][i] == num and pos[1] != i: 
      return False

  # Check column.
  for i in range(len(bo)):
    if bo[i][pos[1]] == num and pos[0] != i: 
      return False
  
  # Check Box of 3 by 3
  box_x = pos[1] // 3
  box_y = pos[0] // 3
  for i in range(box_y*3, box_y*3 + 3): 
    for j in range(box_x*3, box_x*3 + 3):
      if bo[i][j] == num and (i,j) != pos:
        return False
  return True 


def print_board(bo):
  # for loop iterating through each row.  'i' is the row, and 'j' is each value in each row.
  for i in range(len(bo)): 
    if i % 3 == 0 and i != 0: print("- - - - - - - - - - - -")
    
    #iterating through each column of each row.
    for j in range(len(bo[0])): 
      if j % 3 == 0 and j != 0: print(" | ", end="")
        
      if j == 8: print(bo[i][j])
      else: print(bo[i][j], end=" ")

#this finds empty spaces.
def find_empty(bo): 
  for i in range(len(bo)):
    for j in range(len(bo[0])):
      if bo[i][j] == 0:
        return (i, j) 
  return None


# execution
print_board(board)
print('\n\t {}\n'.format(solve(board)))
print_board(board)
