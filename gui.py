import tkinter as tk
from tkinter import ttk

class MicrowaveGui(tk.Tk):  #Create and initialize application with styles
    def __init__(self, title, size):
        # app launch - Main Setup
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        # style manager
        self.styles = StyleManager()
        #add function tabs to notebook
        self.createfunctionwindows = CreateFunctionWindows(self)
        
        # Run program
        self.mainloop()




class CreateFunctionWindows:
    
    def __init__(self, parent):
        self.parent = parent
        self.parent.grid_rowconfigure(1, weight=1)
        self.parent.grid_columnconfigure(0, weight=1)

        # create text box as display on GUI-
        self.displaybox = ttk.Entry(parent, style='DisplayScreen.TEntry')
        self.displaybox.grid(row=0, column=0, sticky='ew', padx=10, pady=10)

        # create notebook for function windows
        self.notebook = ttk.Notebook(parent)
        self.notebook.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)



        # populate tab contents
        self.CreateTimedCook()
        self.CreateDefrost()
        self.CreateCookHistory()

    def CreateTimedCook(self):
        Window = ttk.Frame(self.notebook)
        self.notebook.add(Window, text='Timed Cook')
        ttk.Label(Window, text='Cook controls', style='FunctionLabel.TLabel').grid(row=0, column=0, columnspan=3, pady=10)
        
        # 3x4 button grid (3 columns, 4 rows)
        buttons_data = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9'],
            ['Cancel\nClear', '0', 'Start']
        ]
        
        for row, button_row in enumerate(buttons_data, start=1):
            for col, label in enumerate(button_row):
                if label == 'Cancel\nClear':
                    cmd = self.clear_display
                elif label == 'Start':
                    cmd = lambda: self.button_press('Start')
                else:
                    cmd = lambda num=label: self.button_press(num)
                
                ttk.Button(Window, text=label, style='FunctionButton.TButton', command=cmd).grid(
                    row=row, column=col, padx=12, pady=6
                )
        
    def button_press(self, num):
        """Append number to displaybox"""
        current = self.displaybox.get()
        self.displaybox.delete(0, tk.END)
        self.displaybox.insert(0, str(current) + str(num))

    def clear_display(self):
        """Clear the displaybox"""
        self.displaybox.delete(0, tk.END)


    def CreateDefrost(self):
        Window = ttk.Frame(self.notebook)
        self.notebook.add(Window, text='Defrost')
        ttk.Label(Window, text='Defrost controls', style='FunctionLabel.TLabel').grid(row=0, column=0, pady=10)
     

    def CreateCookHistory(self):
        Window = ttk.Frame(self.notebook)
        self.notebook.add(Window, text='Cook History')
        ttk.Label(Window, text='Run history', style='FunctionLabel.TLabel').grid(row=0, column=0, pady=10)
       

class StyleManager():
    def __init__(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')
        # Label styles
        self.style.configure('FunctionLabel.TLabel',
                            font=('Arial', 12, 'bold'),
                            foreground="#566DD4",
                            background="#9FB6CA",)
        # Button styles
        self.style.configure('FunctionButton.TButton',
                            font=('Arial', 15, 'bold'),
                            foreground="#566DD4",
                            background="#9FB6CA",
                            padding=8)
        
        # increase vertical padding so DisplayScreen entries are taller (≈ +1 row)
        self.style.configure('DisplayScreen.TEntry',
                            font=('Times new roman', 20, 'bold'),
                            justify='right',
                            foreground="#59C26F",
                            fieldbackground="#8FB0CF",
                            padding=(8, 12))
        self.style.configure('TNotebook.Tab',
                            font=('Arial', 15, 'bold'),
                            foreground="#566DD4",
                            background="#9FB6CA",
                            padding=(10, 5))
    








if __name__ == '__main__':
    MicrowaveGui('Microwave System', (500,500))

