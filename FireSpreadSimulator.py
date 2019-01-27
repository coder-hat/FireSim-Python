# 2017-10-21
'''
Toy program that simulates (very simplified) wildfire spread using a simple cellular automata model.
'''
import tkinter as tk
from tkinter import ttk
from FireSimGui import FireSimGui

def main():
    root = tk.Tk()  # meant to be instantiated ONCE per application
    app = FireSimGui(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()
