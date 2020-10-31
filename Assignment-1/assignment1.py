

def read_matrix(filename):
	with open(filename, "r") as f:
		matrix = f.readlines()
		for i,row in enumerate(matrix):
			matrix[i] = list(map(int,matrix[i].split(",")))
	return matrix

def write_matrix(filename, solved_matrix):
	with open(filename, "w") as f:
		f.writelines(','.join(str(j) for j in i) + '\n' for i in solved_matrix)
	print(filename+" for backtracking generated.")

class sudoku():
    def __init__(self, filename):
        self.matrix = read_matrix(filename)
    
    def search_zeros(self):
        sudoku_board=self.matrix
        for i in range(len(sudoku_board)):
            for j in range(len(sudoku_board[0])):
                if(sudoku_board[i][j]==0):
                    return (i,j) #returning the index of the empty box
        return False
    def board_constraints(self, n, index):
        sudoku_board=self.matrix
        #row constraint
        r=index[0]
        c=index[1]
        for j in range(len(sudoku_board[0])):
            if(sudoku_board[r][j]==n):
                return False
        #column constraint
        for i in range(len(sudoku_board)):
            if(sudoku_board[i][c]==n):
                return False
        #3X3 grid constraint
        for i in range((r-(r%3)),3+r-(r%3)):
            for j in range((c-(c%3)),3+c-(c%3)):
                if(sudoku_board[i][j]==n):
                    return False
        return True
    def solve(self):
        ''' WRITE YOUR CODE HERE
			self.matrix contains the 2-D sudoku array.
			Entries having zero need to filled in.
			You can create additional functions that will support this main bactracking function.
		'''
        sudoku_board=self.matrix 
        res=sudoku.search_zeros(self)
        if (not res):
             return True
        else:
             row_empty,col_empty=res
        for n in range(1,10):
            if  sudoku.board_constraints(self, n,(row_empty,col_empty)):
                sudoku_board[row_empty][col_empty]=n
                if sudoku.solve(self):
                    return True
                sudoku_board[row_empty][col_empty]=0
        return False
    def solve_without_backtracking(self):
        ''' WRITE YOUR CODE HERE
			Fill in this function using any algorithm other than backtracking.
			You can implement CSP or any other algo.
        '''

        '''END YOUR CODE HERE'''
        raise NotImplementedError("You need to fill the non-backtracking function") 

if __name__=="__main__":
	su = sudoku("data.txt")
	su.solve()
	write_matrix("sol.txt", su.matrix)
	try:
		su = sudoku("data.txt")
		su.solve_without_backtracking()
		print("Solved sudoku matrix without backtracking:")
		for i in range(9):
			print(*su.matrix[i], sep=" ")
	except Exception as e:
		print(e)
