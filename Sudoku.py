def row_check(array,x,number_toenter):
	for row_element in array[x]:
		if row_element==number_toenter:
			return False
	else:
		return True

def column_check(array,x,y,number_toenter):
	for column_element in [array[x][y] for x in range(9)]:
		if column_element==number_toenter:
			return False
	else:
		return True

def block_check(array,x,y,number_toenter):
	for i in range(x-x%3,(x-x%3)+3):
		for j in range(y-y%3,(y-y%3)+3):
			if array[i][j]==number_toenter:
				return False
	else:
		return True


def number_safety(array,x,y,number_toenter):
	if row_check(array,x,number_toenter):
		if column_check(array,x,y,number_toenter):
			if block_check(array,x,y,number_toenter):
				return True
	return False


def check_emptycells(array):
	for x in range(9):
		for y in range(9):
			if array[x][y]==0:
				return (x,y)
	else:
		return False

def solution(sudoku_array):
	position=check_emptycells(sudoku_array)
	if not position:
		return True
	x,y=position

	for i in range(1,10):
		if number_safety(sudoku_array,x,y,i):
			sudoku_array[x][y]=i
			if solution(sudoku_array):
				return True
			sudoku_array[x][y]=0
			 
	return False
if __name__=='__main__':
	sudoku_array=[[3, 0, 6, 5, 0, 8, 4, 0, 0], 
			[5, 2, 0, 0, 0, 0, 0, 0, 0], 
			[0, 8, 7, 0, 0, 0, 0, 3, 1], 
			[0, 0, 3, 0, 1, 0, 0, 8, 0], 
			[9, 0, 0, 8, 6, 3, 0, 0, 5], 
			[0, 5, 0, 0, 9, 0, 6, 0, 0], 
			[1, 3, 0, 0, 0, 0, 2, 5, 0], 
			[0, 0, 0, 0, 0, 0, 0, 7, 4], 
			[0, 0, 5, 2, 0, 6, 3, 0, 0]]

	Answer_Key='''	3 1 6 5 7 8 4 9 2
					5 2 9 1 3 4 7 6 8
					4 8 7 6 2 9 5 3 1
					2 6 3 4 1 5 9 8 7
					9 7 4 8 6 3 1 2 5
					8 5 1 7 9 2 6 4 3
					1 3 8 9 4 7 2 5 6
					6 9 2 3 5 1 8 7 4
					7 4 5 2 8 6 3 1 9	'''

	Result=solution(sudoku_array)
	if Result:
		print(sudoku_array)
	else:
		print('Error',Result)