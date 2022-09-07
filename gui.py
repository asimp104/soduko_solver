from turtle import update
import soduko_solver
from tkinter import *

root = Tk()
root.title("Soduko Solver")
root.geometry("324x520")

label = Label(root, text="Fill in the numbers and click solve").grid(row=0, column=1, columnspan=10)

errLabel = Label(root, text="", fg="red")
errLabel.grid(row=15, column=1, columnspan=10, pady=5)

solvedLabel = Label(root, text="", fg="green")
solvedLabel.grid(row=15, column=1, columnspan=10, pady=5)

cells = {}

def validate_number(P):
    return P.isdigit() and len(P)<2

reg = root.register(validate_number)

def draw_3x3_grid(row, column, bgcolor):
    for i in range(3):
        for j in range(3):
            e = Entry(root, width=5, bg=bgcolor, justify='center', validate='key', validatecommand=(reg, "%P"))
            e.grid(row=row+i+1, column=column+j+1, sticky="nsew", padx=1, pady=1, ipady=5)
            cells[(row+i+1, column+j+1)] = e

def draw_9x9_grid():
    color = "#D0ffff"
    for rowNo in range(1,10,3):
        for colNo in range(0,9,3):
            draw_3x3_grid(rowNo, colNo, color)
            if color == "#D0ffff":
                color = "#ffffD0"
            else:
                color = "#D0ffff"


def clear_values():
    errLabel.configure(text="")
    solvedLabel.configure(text="")
    for row in range(2,11):
        for col in range(1,10):
            cells[(row,col)].delete(0,END)

            

def get_values():
    board=[]
    errLabel.configure(text="")
    solvedLabel.configure(text="")
    for row in range(2,11):
        rows = []
        for col in range(1,10):
            val = cells[(row,col)].get()
            if val == "":
                rows.append(0)
            else:
                rows.append(val)
        board.append(rows)
    update_values(board)

def update_values(board):
    sol = soduko_solver.solver(board)
    if sol != "no":
        for row in range(2,11):
            for col in range(1,10):
                cells[(row,col)].delete(0,END)
                cells[(row,col)].insert(0, board[row-2][col-1])
                solvedLabel.configure(text="Solved!")
    else:
        errLabel.configure(text="No solution exists for this soduko :(")

btn = Button(root, command=get_values, text="Solve", width=10)
btn.grid(row=20, column=1, columnspan=5)

btn = Button(root, command=clear_values, text="Clear", width=10)
btn.grid(row=20, column=5, columnspan=5)

draw_9x9_grid()
root.mainloop()

    
    


