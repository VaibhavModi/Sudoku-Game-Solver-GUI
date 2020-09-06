import tkinter as tk
from tkinter import messagebox


class Sudoku_Solver:

    def row_check(self, x, number_toenter):
        for row_element in sudoku_array[x]:
            if row_element == number_toenter:
                return False
        else:
            return True

    def column_check(self, y, number_toenter):
        for column_element in [sudoku_array[x][y] for x in range(9)]:
            if column_element == number_toenter:
                return False
        else:
            return True

    def block_check(self, x, y, number_toenter):
        for i in range(x - x % 3, (x - x % 3) + 3):
            for j in range(y - y % 3, (y - y % 3) + 3):
                if sudoku_array[i][j] == number_toenter:
                    return False
        else:
            return True

    def number_safety(self,x, y, number_toenter):
        if self.row_check(x, number_toenter):
            if self.column_check(y, number_toenter):
                if self.block_check(x, y, number_toenter):
                    return True
        return False

    def check_emptycells(self):
        for x in range(9):
            for y in range(9):
                if sudoku_array[x][y] == 0:
                    return (x, y)
        else:
            return False

    def solution(self):
        position = self.check_emptycells()
        if not position:
            return True
        x, y = position

        for i in range(1, 10):
            if self.number_safety(x, y, i):
                sudoku_array[x][y] = i
                entrybox_list[x][y].insert(0, i)
                if self.solution():
                    return True
                sudoku_array[x][y] = 0
                entrybox_list[x][y].delete(0, 'end')
        return False


class draw_window:

    global entrybox_list, var
    entrybox_list = []

    def __init__(self, master):
        master.geometry('505x520')
        master.title('Sudoku Solver')
        master.resizable(False, False)
        master.configure(bg='peachpuff')
        self.master=master
        self.var = tk.IntVar()
        self.upper_frame(master)
        self.lower_frame(master)

    def upper_frame(self, master):
        global solve_bt
        frame1 = tk.Frame(master, bg='peachpuff')
        label1 = tk.Label(frame1,fg='purple', bg='silver',text='>> To solve a Sudoku, fill up the board and press solve <<', font=('MS Serif', 14)).pack(side='top', anchor='w', padx=20, pady=(10, 1))
        solve_bt = tk.Button(frame1, text='Solve', height=1, width=5, font=('Helvetica', 15, 'bold'),
                             command=lambda: self.solve(), bg='orange', fg='White', padx=0)
        solve_bt.pack(side='left',
                      anchor='sw',
                      padx=(15, 10),
                      pady=(0, 20))
        clear_bt = tk.Button(frame1, text='Clear All', height=1, width=7, font=('Helvetica', 15, 'bold'),
                             command=lambda: self.clear(), bg='orange', fg='White', padx=0)
        clear_bt.pack(side='left',
                      anchor='se',
                      padx=(20, 10),
                      pady=(0, 20))
        frame1.grid(column=0, row=0, padx=(0, 20), pady=(0, 1), sticky='w', ipady=20, ipadx=150)

    # Sudoku 9x9 Board
    def lower_frame(self, master):

        frame2 = tk.Frame(master,bg='gray')
        val=frame2.register(self.validate)
        for row in range(9):
            entrybox_list.append([])
            for column in range(9):
                temp = tk.Entry(frame2, width=3, justify='center', font=('Helvetica', 17), borderwidth=2, relief="ridge",
                                fg='blue')
                temp.configure(validate='key',validatecommand=(val,'%P'))
                temp.grid(column=column, row=row, ipady=4, ipadx=4)
                entrybox_list[row].append(temp)

        for row in range(9):    # Creating spaces between box grid for black bar seperating 3x3 blocks
            entrybox_list[row][2].grid(row=row,column=2,ipady=4, ipadx=4,padx=(0,3))
            entrybox_list[row][5].grid(row=row,column=5,ipady=4, ipadx=4,padx=(0,3))
            entrybox_list[2][row].grid(row=2,column=row,ipady=4, ipadx=4,pady=(0,3))
            entrybox_list[5][row].grid(row=5,column=row,ipady=4, ipadx=4,pady=(0,3))
        frame2.grid(column=0, row=1, padx=10, pady=(15, 10), sticky='w')


    def solve(self):
        for i in range(9):
            sudoku_array.append([])
            for j in range(9):
                if entrybox_list[i][j].get() == '':
                    sudoku_array[i].append(0)
                    entrybox_list[i][j].configure(fg='green')
                else:
                    sudoku_array[i].append(int(entrybox_list[i][j].get()))
                    entrybox_list[i][j].configure(fg='blue')


        solve_bt.configure(state='disable')
        self.master.focus()
        Sudoku_SolverObj=Sudoku_Solver()
        Sudoku_SolverObj.solution()

    def clear(self):
        for entries in entrybox_list:
            if sudoku_array:
                sudoku_array.pop()
            for entry in entries:
                entry.delete(0, 'end')
                entry.configure(fg='blue')
        solve_bt.configure(state='normal')
        self.master.focus()

    #Validation of input in the Sudoku Grid
    def validate(self,input):
        if input=='':
            return True
        if len(input)>1 or not input.isdigit():
            messagebox.showerror('Sudoku','Only single digit numerical entry is allowed!')
            return False
        else:
            return True

if __name__ == '__main__':

    sudoku_array = []

    window_app = tk.Tk()
    draw_window(window_app)
    window_app.mainloop()