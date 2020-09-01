import tkinter as tk
import time

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

def solution():
	position=check_emptycells(sudoku_array)
	if not position:
		return True
	x,y=position

	for i in range(1,10):
		if number_safety(sudoku_array,x,y,i):
			sudoku_array[x][y]=i
			entrybox_list[x][y].insert(0,i)
			if solution():
				return True
			sudoku_array[x][y]=0
			entrybox_list[x][y].delete(0,'end')
	return False


class draw_window:
	global entrybox_list, var
	entrybox_list=[]

	def __init__(self, master):
		master.geometry('500x520')
		master.title('Sudoku Solver')
		master.resizable(False, False)
		self.var=tk.IntVar()
		self.upper_frame(master)
		self.lower_frame(master)

	def upper_frame(self,master):
		global button1
		frame1=tk.Frame(master)
		label1 = tk.Label(frame1,text='>     To solve a Sudoku, fill up the board and press solve',font=('Times New Roman',14)).pack(side='top',anchor='w')
		button1 = tk.Button(frame1,text='Solve', height=2,width=10, font=('Times New Roman',12,'bold') ,command=lambda: self.solve(),fg='blue').pack(side='left', anchor='sw',padx=190)
		frame1.grid(column=0,row=0, padx=10,pady=(10,1),sticky='w',ipady=20,ipadx=150)

	# Sudoku 9x9 Board
	def lower_frame(self,master):
		frame2 = tk.Frame(master)
		for row in range(9):
			entrybox_list.append([])
			for column in range(9):
				temp = tk.Entry(frame2, width=3,justify='center',font=('Arial',17))
				temp.grid(column=column,row=row,ipady=5,ipadx=5)
				entrybox_list[row].append(temp)
		frame2.grid(column=0,row=1,padx=10,pady=(15,10),sticky='w')

	def solve(self):
		for i in range(9):
			sudoku_array.append([])
			for j in range(9):
				if entrybox_list[i][j].get() =='':
					sudoku_array[i].append(0)
					entrybox_list[i][j].configure(fg='green')
				else:
					sudoku_array[i].append(int(entrybox_list[i][j].get()))
					entrybox_list[i][j].configure(fg='blue')
		solution()

	def solve1(self):
		pass

if __name__=='__main__':
	sudoku_array=[]

	'''sudoku_array=[[0, 0, 6, 0, 0, 7, 0, 0, 0],
				[2, 8, 5, 0, 0, 0, 0, 0, 0],
				[0, 0, 4, 9, 0, 6, 0, 0, 0],
				[1, 0, 0, 0, 0, 0, 0, 6, 0],
				[0, 0, 0, 0, 1, 3, 9, 0, 0],
				[0, 2, 0, 0, 0, 0, 4, 0, 0],
				[4, 0, 8, 5, 0, 0, 0, 0, 2],
				[0, 0, 0, 8, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 6, 0, 0, 8, 5]]'''

	window_app= tk.Tk()
	drawing_object=draw_window(window_app)
	window_app.mainloop()

	'''Result=solution()
	if Result:
		print(sudoku_array)
	else:
		print('Error',Result)'''