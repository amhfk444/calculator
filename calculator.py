import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator App")
        
        self.math_process = []
        
        # Define colors
        bg_color = "#f0f0f0"  # Light gray
        button_bg_color = "#ffffff"  # White
        button_fg_color = "#000000"  # Black
        
        self.root.config(bg=bg_color)
        
        self.task_entry = tk.Entry(root, width=30, bg=button_bg_color)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)
        
        self.content_label = tk.Label(root, text="Content:", bg=bg_color)
        self.content_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        
        # Define button colors
        button_colors = {"bg": button_bg_color, "fg": button_fg_color}
        
        self.num1_butt = tk.Button(root, text="1", command=self.num1_text, width=5, height=2, **button_colors)
        self.num1_butt.grid(row=1, column=1, padx=10, pady=10)
        
        self.num2_butt = tk.Button(root, text="2", command=self.num2_text, width=5, height=2, **button_colors)
        self.num2_butt.grid(row=1, column=2, padx=10, pady=10)
        
        self.num3_butt = tk.Button(root, text="3", command=self.num3_text, width=5, height=2, **button_colors)
        self.num3_butt.grid(row=1, column=3, padx=10, pady=10)

        # Add more buttons with colors
        
        self.num4_butt = tk.Button(root, text="4", command=self.num4_text, width=5, height=2, **button_colors)
        self.num4_butt.grid(row=2, column=1, padx=10, pady=10)

        self.num5_butt = tk.Button(root, text="5", command=self.num5_text, width=5, height=2, **button_colors)
        self.num5_butt.grid(row=2, column=2, padx=10, pady=10)

        self.num6_butt = tk.Button(root, text="6", command=self.num6_text, width=5, height=2, **button_colors)
        self.num6_butt.grid(row=2, column=3, padx=10, pady=10)

        self.num7_butt = tk.Button(root, text="7", command=self.num7_text, width=5, height=2, **button_colors)
        self.num7_butt.grid(row=3, column=1, padx=10, pady=10)

        self.num8_butt = tk.Button(root, text="8", command=self.num8_text, width=5, height=2, **button_colors)
        self.num8_butt.grid(row=3, column=2, padx=10, pady=10)

        self.num9_butt = tk.Button(root, text="9", command=self.num9_text, width=5, height=2, **button_colors)
        self.num9_butt.grid(row=3, column=3, padx=10, pady=10)

        self.num0_butt = tk.Button(root, text="0", command=self.num0_text, width=5, height=2, **button_colors)
        self.num0_butt.grid(row=4, column=1, padx=10, pady=10)
        
        self.add_butt = tk.Button(root, text="+", command=self.add_butt_text, width=5, height=2, **button_colors)
        self.add_butt.grid(row=3, column=4, padx=10, pady=10)

        self.sub_butt = tk.Button(root, text="-", command=self.sub_butt_text, width=5, height=2, **button_colors)
        self.sub_butt.grid(row=4, column=2, padx=10, pady=10)

        self.mult_butt = tk.Button(root, text="*", command=self.mult_butt_text, width=5, height=2, **button_colors)
        self.mult_butt.grid(row=4, column=3, padx=10, pady=10)

        self.div_butt = tk.Button(root, text="/", command=self.div_butt_text, width=5, height=2, **button_colors)
        self.div_butt.grid(row=1, column=4, padx=10, pady=10)
        
        
        self.equals_butt = tk.Button(root, text="=", command=self.equals_butt_text, width=5, height=2, **button_colors)
        self.equals_butt.grid(row=4, column=4, padx=10, pady=10)
        
        
        self.clear_butt = tk.Button(root, text="Clear", command=self.clear_butt_text, width=5, height=2, **button_colors)
        self.clear_butt.grid(row=2, column=4, padx=10, pady=10)

        

    def num1_text(self):
        current_text = self.task_entry.get()
        self.task_entry.delete(0, tk.END)
        self.task_entry.insert(tk.END, current_text + "1")
        
    def num2_text(self):
        current_text = self.task_entry.get()
        self.task_entry.delete(0, tk.END)
        self.task_entry.insert(tk.END, current_text + "2")
        
    def num3_text(self):
        current_text = self.task_entry.get()
        self.task_entry.delete(0, tk.END)
        self.task_entry.insert(tk.END, current_text + "3")
        
    def num4_text(self):
        current_text = self.task_entry.get()
        self.task_entry.delete(0, tk.END)
        self.task_entry.insert(tk.END, current_text + "4")
        
    def num5_text(self):
        current_text = self.task_entry.get()
        self.task_entry.delete(0, tk.END)
        self.task_entry.insert(tk.END, current_text + "5")
        
    def num6_text(self):
        current_text = self.task_entry.get()
        self.task_entry.delete(0, tk.END)
        self.task_entry.insert(tk.END, current_text + "6")
        
    def num7_text(self):
        current_text = self.task_entry.get()
        self.task_entry.delete(0, tk.END)
        self.task_entry.insert(tk.END, current_text + "7")
        
    def num8_text(self):
        current_text = self.task_entry.get()
        self.task_entry.delete(0, tk.END)
        self.task_entry.insert(tk.END, current_text + "8")
        
    def num9_text(self):
        current_text = self.task_entry.get()
        self.task_entry.delete(0, tk.END)
        self.task_entry.insert(tk.END, current_text + "9")
    
    def num0_text(self):
        current_text = self.task_entry.get()
        self.task_entry.delete(0, tk.END)
        self.task_entry.insert(tk.END, current_text + "0")
        
    def add_butt_text(self):
        current_text = self.task_entry.get()
        self.task_entry.delete(0, tk.END)
        self.task_entry.insert(tk.END, current_text + "+")

    def sub_butt_text(self):
        current_text = self.task_entry.get()
        self.task_entry.delete(0, tk.END)
        self.task_entry.insert(tk.END, current_text + "-")

    def mult_butt_text(self):
        current_text = self.task_entry.get()
        self.task_entry.delete(0, tk.END)
        self.task_entry.insert(tk.END, current_text + "*")

    def div_butt_text(self):
        current_text = self.task_entry.get()
        self.task_entry.delete(0, tk.END)
        self.task_entry.insert(tk.END, current_text + "/")
        
        
    def equals_butt_text(self):
        expression = self.task_entry.get()
        result = eval(expression)
        self.task_entry.delete(0, tk.END)
        self.task_entry.insert(tk.END, str(result))
        
        
    def clear_butt_text(self):
        self.task_entry.delete(0, tk.END)
        

if __name__ == "__main__":
    root = tk.Tk() 
    app = CalculatorApp(root)
    root.mainloop()
