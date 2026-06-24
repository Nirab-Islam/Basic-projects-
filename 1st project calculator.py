```python
import tkinter as tk

# ==========================================
# CORE CALCULATION LOGIC (English Comments)
# ==========================================

def button_click(char):
    """Appends the clicked button character to the display screen."""
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(char))

def clear_screen():
    """Clears the entire display screen."""
    entry.delete(0, tk.END)

def backspace():
    """Deletes only the last character on the screen (one by one)."""
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def calculate():
    """Evaluates the math expression on the screen and shows the result."""
    try:
        # eval() automatically computes the mathematical expression string
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        # If there's an invalid expression, display 'Error' safely instead of crashing
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# ==========================================
# GUI WINDOW SETUP & CUSTOM STYLING
# ==========================================

root = tk.Tk()
root.title("Aesthetic Gray Calculator")
root.configure(bg="#2d3436")  # Premium dark gray background for the main window
root.geometry("380x550")
root.resizable(False, False)

# Configure responsive rows and columns for uniform button sizing
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# ==========================================
# DISPLAY SCREEN SETUP
# ==========================================

entry = tk.Entry(
    root, 
    font=("Consolas", 24), 
    bg="#1e1e1e",      # Deep dark gray/black display screen
    fg="#ffffff",      # Clear white text for calculations
    bd=0, 
    justify="right", 
    insertbackground="#ffffff"  # White cursor
)
# Adding padding to make the display look spacious and aligned
entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=15, pady=20)

# ==========================================
# BUTTON LAYOUT AND SPECIFIC COLOR PALETTES
# ==========================================

# Format: (Text, Row, Column, Button Type)
buttons_layout = [
    ('C', 1, 0, 'clear'), ('⌫', 1, 1, 'back'), ('(', 1, 2, 'op'), (')', 1, 3, 'op'),
    ('7', 2, 0, 'num'),   ('8', 2, 1, 'num'),  ('9', 2, 2, 'num'),  ('/', 2, 3, 'op'),
    ('4', 3, 0, 'num'),   ('5', 3, 1, 'num'),  ('6', 3, 2, 'num'),  ('*', 3, 3, 'op'),
    ('1', 4, 0, 'num'),   ('2', 4, 1, 'num'),  ('3', 4, 2, 'num'),  ('-', 4, 3, 'op'),
    ('0', 5, 0, 'num'),   ('.', 5, 1, 'num'),  ('=', 5, 2, 'equal'),('+', 5, 3, 'op')
]

# Generate and mount all customized buttons onto the grid
for (text, row, col, btn_type) in buttons_layout:
    # Set default values
    bg_color = "#ffffff"
    fg_color = "#2d3436"
    cmd = lambda t=text: button_click(t)

    # Style customizations as requested:
    if btn_type == 'num':
        bg_color = "#ffffff"   # Number buttons are pure white
        fg_color = "#2d3436"   # Text on white buttons is dark gray for high readability
    elif btn_type == 'op':
        bg_color = "#00b4d8"   # Sky blue / Cyanish color for operators
        fg_color = "#ffffff"   # White operator labels
    elif btn_type == 'back':
        bg_color = "#ff4d4d"   # Vibrant Red color for the single-character backspace button
        fg_color = "#ffffff"   # White delete arrow/text
        cmd = backspace
    elif btn_type == 'clear':
        bg_color = "#7f8c8d"   # Medium gray for full-clear button to keep it distinct
        fg_color = "#ffffff"   
        cmd = clear_screen
    elif btn_type == 'equal':
        bg_color = "#2ecc71"   # Soft Green color for the equals operator
        fg_color = "#ffffff"   
        cmd = calculate

    # Creating the Tkinter button with smooth active states
    btn = tk.Button(
        root, 
        text=text, 
        font=("Consolas", 18, "bold"), 
        bg=bg_color, 
        fg=fg_color, 
        activebackground=bg_color, 
        activeforeground=fg_color, 
        bd=0, 
        command=cmd
    )
    btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# ==========================================
# APPLICATION START
# ==========================================

if __name__ == "__main__":
    root.mainloop()

```
