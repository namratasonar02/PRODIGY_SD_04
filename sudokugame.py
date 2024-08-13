import tkinter as tk
from tkinter import messagebox

class SudokuSolver:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Sudoku Solver")
        self.window.configure(bg="#000000")  # black background

        # Create a main frame to hold both the grid and the solution
        self.main_frame = tk.Frame(self.window, bg="#000000")
        self.main_frame.pack(padx=20, pady=20)

        # Create a frame for the Sudoku grid
        self.grid_frame = tk.Frame(self.main_frame, bg="#000000", width=300, height=300)
        self.grid_frame.grid(row=0, column=0, padx=20, pady=20)

        # Create a 9x9 grid of entry fields
        self.entries = []
        for i in range(9):
            row = []
            for j in range(9):
                entry = tk.Entry(self.grid_frame, width=2, font=("Arial", 18), bg="#CCCCCC", fg="#000000")
                entry.grid(row=i, column=j, padx=2, pady=2)
                row.append(entry)
            self.entries.append(row)

        # Create a frame for the solved answer grid
        self.answer_frame = tk.Frame(self.main_frame, bg="#000000", width=300, height=300)
        self.answer_frame.grid(row=0, column=1, padx=20, pady=20)

        # Create a button to solve the puzzle
        self.solve_button = tk.Button(self.window, text="Solve", command=self.solve, font=("Arial", 18), bg="#4CAF50", fg="#FFFFFF")
        self.solve_button.pack(pady=20)

        # Create a label to display the solution status
        self.solution_label = tk.Label(self.window, text="", font=("Arial", 18), bg="#000000", fg="#FFFFFF")
        self.solution_label.pack(pady=10)

    def solve(self):
        # Get the input grid from the entry fields
        grid = []
        for row in self.entries:
            grid_row = []
            for entry in row:
                value = entry.get()
                if value:
                    grid_row.append(int(value))
                else:
                    grid_row.append(0)
            grid.append(grid_row)

        # Solve the puzzle using backtracking
        if self.solve_sudoku(grid):
            # Display the solution
            self.display_solution(grid)
            # Display the solved puzzle answer
            self.display_answer(grid)
        else:
            messagebox.showerror("Error", "No solution found")

    def solve_sudoku(self, grid):
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    for value in range(1, 10):
                        if self.is_valid(grid, i, j, value):
                            grid[i][j] = value
                            if self.solve_sudoku(grid):
                                return True
                            grid[i][j] = 0
                    return False
        return True

    def is_valid(self, grid, row, col, value):
        # Check if the value is already present in the row or column
        for i in range(9):
            if grid[row][i] == value or grid[i][col] == value:
                return False

        # Check if the value is already present in the 3x3 sub-grid
        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if grid[start_row + i][start_col + j] == value:
                    return False

        return True

    def display_solution(self, grid):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, "end")
                self.entries[i][j].insert(0, str(grid[i][j]))
        self.solution_label.config(text="Solution found!")

    def display_answer(self, grid):
        # Clear previous answers
        for widget in self.answer_frame.winfo_children():
            widget.destroy()

        # Display the solved puzzle answer in blocks
        for i in range(9):
            for j in range(9):
                label = tk.Label(self.answer_frame, text=str(grid[i][j]), font=("Arial", 18), width=2, bg="#333333", fg="#FFFFFF")
                label.grid(row=i, column=j, padx=2, pady=2)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    solver = SudokuSolver()
    solver.run()
