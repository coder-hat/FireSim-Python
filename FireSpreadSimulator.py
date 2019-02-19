# 2017-10-21
'''
Toy program that simulates wildfire spread using a simple cellular automata model.
FireSpreadSimulator provides the __main__ entry point for a runtime-specified FireSim engine type.
'''
import argparse
import tkinter as tk
from tkinter import ttk
from FireSimGui import FireSimGui
from FireSimEngine import FireSimEngine
from FireSimFueledEngine import FireSimFueledEngine


def main():

    parser = argparse.ArgumentParser(description="Run FireSpread Simulator With Specified Engine")
    parser.add_argument('--engine', nargs='?', choices=['original', 'fueled'], default='original', const='original', help='The simulator engine to use')

    args = parser.parse_args()

    simEngine = 'original'
    if args.engine == 'original':
        simEngine = FireSimEngine()
    elif args.engine == 'fueled':
        simEngine = FireSimFueledEngine()
    assert simEngine
    
    root = tk.Tk()  # instantiated ONCE per application
    app = FireSimGui(master=root, engine=simEngine)    
    app.mainloop()

if __name__ == "__main__":
    main()
