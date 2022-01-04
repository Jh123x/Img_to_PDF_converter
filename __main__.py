from tkinter import Tk
from GUI.Window import Window, DEFAULT_WINDOW_TITLE


def main():
    '''The main function for the PDF Toolkit in Python to run the GUI'''
    root = Tk()
    # Setting the size of the root window
    root.geometry("")
    root.minsize = (1000, 500)
    root.title = DEFAULT_WINDOW_TITLE
    w = Window(root)
    w.grid(sticky="nsew")
    w.columnconfigure(4, weight=1)

    root.mainloop()


if __name__ == "__main__":
    main()
