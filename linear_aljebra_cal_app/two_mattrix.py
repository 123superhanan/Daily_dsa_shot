import tkinter as tk
from tkinter import ttk, messagebox
from unittest import result
import numpy as np  # pip install numpy

class MatrixApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Matrix Beast - Tkinter Edition")
        self.root.geometry("900x700")
        self.root.configure(bg="#222")

        # Style
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 12), padding=8)
        style.configure("TLabel", font=("Helvetica", 14), background="#222", foreground="white")

        # Frames
        self.frame_left  = tk.Frame(root, bg="#222", padx=20, pady=20)
        self.frame_right = tk.Frame(root, bg="#222", padx=20, pady=20)
        self.frame_left.grid(row=0, column=0, sticky="n")
        self.frame_right.grid(row=0, column=1, sticky="n")

        # Matrix A (left)
        # Matrix A (left) – use grid for everything
        tk.Label(self.frame_left, text="Matrix A", font=("Helvetica", 18, "bold"), bg="#222", fg="#0f0") \
        .grid(row=0, column=0, columnspan=3, pady=(0, 10), sticky="ew")
        self.entries_A = self.create_matrix_grid(self.frame_left, 3, 3, start_row=1)

        # Matrix B or vector (right) - start with 3x3
        tk.Label(self.frame_right, text="Matrix B / Vector b", font=("Helvetica", 18, "bold"), bg="#222", fg="#0f0") \
        .grid(row=0, column=0, columnspan=3, pady=(0, 10), sticky="ew")
        self.entries_B = self.create_matrix_grid(self.frame_right, 3, 3, start_row=1)

        # Buttons area (bottom)
        btn_frame = tk.Frame(root, bg="#222")
        btn_frame.grid(row=1, column=0, columnspan=2, pady=20)

        ops = [
            ("A + B", self.add_matrices),
            ("A - B", self.subtract_matrices),
            ("A × B", self.multiply_matrices),
            ("Transpose A", self.transpose_A),
            ("Det A", self.det_A),
            ("Inverse A", self.inverse_A),
            # We'll add Cramer's, Adjoint, RREF later
        ]

        for i, (text, cmd) in enumerate(ops):
            ttk.Button(btn_frame, text=text, command=cmd).grid(row=i//3, column=i%3, padx=10, pady=10, ipadx=10)

        # Result display
        self.result_text = tk.Text(root, height=10, width=80, font=("Consolas", 12), bg="#111", fg="#0f0")
        self.result_text.grid(row=2, column=0, columnspan=2, padx=20, pady=10)
    def create_matrix_grid(self, parent, rows, cols, start_row=0):
        entries = []
        for i in range(rows):
            row = []
            for j in range(cols):
                e = tk.Entry(parent, width=6, font=("Consolas", 14), justify="center")
                e.grid(row=start_row + i, column=j, padx=3, pady=3)
                row.append(e)
            entries.append(row)
        return entries
    def get_matrix(self, entries):
        mat = []
        for row in entries:
            row_vals = []
            for e in row:
                val = e.get().strip()
                if val == "":
                    messagebox.showerror("Input Error", "All fields must be filled!")
                    return None
                try:
                    row_vals.append(float(val))
                except ValueError:
                    messagebox.showerror("Input Error", "Invalid number!")
                    return None
            mat.append(row_vals)
        return np.array(mat)

    # Placeholder operations (we'll fill them next)
    def add_matrices(self):
        A = self.get_matrix(self.entries_A)
        B = self.get_matrix(self.entries_B)
        if A is None or B is None: return
        if A.shape != B.shape:
            messagebox.showerror("Shape Error", "Matrices must have same dimensions!")
            return
        result = A + B
        self.show_result(result)
    def det_A(self):
            A = self.get_matrix(self.entries_A)
            if A is None:
                return
            
            rows, cols = A.shape
            if rows != cols:
                messagebox.showerror("Error", "Matrix must be square for determinant!")
                return
            
            if rows == 1:
                result = A[0,0]
            elif rows == 2:
                result = self.det_2x2(A)
            elif rows == 3:
                result = self.det_3x3_sarrus(A)     # or self.det_3x3_cofactor(A)
            else:
                messagebox.showerror("Error", "Only 1×1, 2×2, 3×3 supported with basic NumPy")
                return
                self.show_result(f"det(A) = {result:.4f}")
    # Optional: color feedback
            if abs(result) < 1e-8:
                self.result_text.tag_add("singular", "1.0", "end")
                self.result_text.tag_config("singular", foreground="red")
            else:
                self.result_text.tag_config("singular", foreground="#0f0")
    def show_result(self, mat):
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "Result:\n" + str(mat))
    # More stubs (add later)
    def subtract_matrices(self): pass
    def multiply_matrices(self): pass
    def transpose_A(self): pass
    def det_A(self): pass
    def inverse_A(self): pass

if __name__ == "__main__":
    root = tk.Tk()
    app = MatrixApp(root)
    root.mainloop()