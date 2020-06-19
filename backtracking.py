"""回溯算法：
递归，渐进的创建解决方案，任何时间步，删除不满足问题限制条件的解决方案。
解数独时，当当前数值不可能获得解时，删除该值（回溯），尝试下一个数值
"""

"""一、The Knight’s tour problem
在一个N*M的棋盘上，在任意位置放置一个骑士，骑士只能走"日字"，和象棋中的马一样。
问该骑士能否不重复遍历整个棋盘。
"""


class KnightTour:
    def __init__(self, n):
        self.n = n
    
    def isSafe(self, x, y, board):
        if (x >= 0 and y >= 0 and x < self.n and y < self.n and board[x][
            y] == -1):
            return True
        return False
    
    def printSolution(self, board):
        for i in range(self.n):
            for j in range(self.n):
                print(board[i][j], end=' ')
            print()
    
    def solve(self):
        # 棋盘初始
        board = [[-1 for _ in range(self.n)] for _ in range(self.n)]
        
        # 可移动方向
        move_x = [2, 1, -1, -2, -2, -1, 1, 2]
        move_y = [1, 2, 2, 1, -1, -2, -2, -1]
        
        # 骑士的初始位置
        board[0][0] = 0
        
        # 骑士的步数
        pos = 1
        
        # 检查解是否存在
        if not self.solveKT(board, 0, 0, move_x, move_y, pos):
            print("Solution does not exist")
        else:
            self.printSolution(board)
    
    def solveKT(self, board, curr_x, curr_y, move_x, move_y, pos):
        if pos == self.n ** 2:
            return True
        
        for i in range(8):
            new_x = curr_x + move_x[i]
            new_y = curr_y + move_y[i]
            if self.isSafe(new_x, new_y, board):
                board[new_x][new_y] = pos
                if self.solveKT(board, new_x, new_y, move_x, move_y, pos + 1):
                    return True
                
                # 回溯：还原状态，尝试下一个方案
                board[new_x][new_y] = -1
        return False


# KnightTour(6).solve()

"""二、Rat in a Maze
给定矩阵，0 表示阻塞，1 表示可通行。老鼠只能向右或向下移动，从左上角出发，是否能走到右下角。
"""


class Maze:
    def __init__(self, maze):
        self.maze = maze
        self.size = len(self.maze)
    
    def printSolution(self, sol):
        for i in sol:
            for j in i:
                print(str(j) + " ", end="")
            print("")
    
    def isSafe(self, x, y):
        if x >= 0 and x < self.size and y >= 0 and y < self.size and \
                self.maze[x][y] == 1:
            return True
        return False
    
    def solve(self):
        sol = [[0 for _ in range(self.size)] for _ in range(self.size)]
        
        if not self.solveMaze(0, 0, sol):
            print("Solution doesn't exist")
            return False
        self.printSolution(sol)
        return True
    
    def solveMaze(self, x, y, sol):
        if x == self.size - 1 and y == self.size - 1:
            sol[x][y] = 1
            return True
        
        if self.isSafe(x, y):
            sol[x][y] = 1
            
            if self.solveMaze(x + 1, y, sol):
                return True
            
            if self.solveMaze(x, y + 1, sol):
                return True
            
            sol[x][y] = 0
            return False


maze = [[1, 1, 0, 0], [0, 1, 1, 1], [0, 1, 0, 1], [1, 0, 1, 1]]
# Maze(maze).solve()


"""三、数独
"""
# TODO: https://www.geeksforgeeks.org/sudoku-backtracking-7/

class Sudoku:
    
    def print_grid(self, arr):
        for i in range(9):
            for j in range(9):
                print(arr[i][j])
            print('\n')
    
    def find_empty_location(self, arr, l):
        for row in range(9):
            for col in range(9):
                if arr[row][col] == 0:
                    l[0] = row
                    l[1] = col
                    return True
        return False
    
    def used_in_row(self, arr, row, num):
        for i in range(0):
            if arr[row][i] == num:
                return True
        return False
    
    def used_in_col(self, arr, col, num):
        for i in range(9):
            if arr[i][col] == num:
                return True
        return False
    
    def used_in_box(self, arr, row, col, num):
        for i in range(3):
            for j in range(3):
                if arr[i + row][j + col] == num:
                    return True
        return False
    
    def check_location_is_safe(self, arr, row, col, num):
        return not self.used_in_box(arr, row, col,
            num) and not self.used_in_row(arr, row,
            num) and not self.used_in_col(arr, col, num)
    
    def solve(self, arr):
        l = [0, 0]
        
        if (not self.find_empty_location(arr, l)):
            return True
        
        row = l[0]
        col = l[1]
        
        for num in range(1, 10):
            if self.check_location_is_safe(arr, row, col, num):
                arr[row][col] = num
                if self.solve(arr):
                    return True
                arr[row][col] = 0
        
        return False
    
grid=[[3,0,6,5,0,8,4,0,0],
      [5,2,0,0,0,0,0,0,0],
      [0,8,7,0,0,0,0,3,1],
      [0,0,3,0,1,0,0,8,0],
      [9,0,0,8,6,3,0,0,5],
      [0,5,0,0,9,0,6,0,0],
      [1,3,0,0,0,0,2,5,0],
      [0,0,0,0,0,0,0,7,4],
      [0,0,5,2,0,6,3,0,0]]
Sudoku().solve(grid)
