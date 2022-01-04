from tkinter import Frame, Label, Entry, Button, StringVar, Checkbutton, Tk, X
from tkinter.constants import DISABLED
from tkinter.filedialog import askopenfilenames

from Core import convert_files
from Core.constants import NO_FILES_SELECTED
from GUI.constants import BROWSE_STRING, EMPTY_STRING, FILE_TYPES, SUBMIT_STRING, DEFAULT_WINDOW_TITLE, INSTRUCTIONS


class Window(Frame):
    '''The main class for the tkinter window'''

    def __init__(self, master: Tk):
        """The main window for the PDF converter"""
        super().__init__(master)
        self.selected_files = None
        self.create_widgets()

    def _select_file(self, paths: tuple[str]) -> None:
        """Store selected files and update the textbox"""
        self.loc.set(str(paths)[1:-1])
        self.selected_files = paths

    def _convert_files(self) -> None:
        """Convert the selected files to a PDF"""
        if self.selected_files is None or type(self.selected_files) is not tuple:
            message = NO_FILES_SELECTED
        else:
            message = convert_files(self.selected_files)
        self.status_text.set(message)

    def create_widgets(self):
        """Create the widgets within the window"""

        # Creating the top Label for the GUI Window
        self.label = Label(text=DEFAULT_WINDOW_TITLE)

        # Create a status bar to see the status
        self.status_text = StringVar()
        self.status = Label(textvariable=self.status_text)
        self.status_text.set(INSTRUCTIONS)

        # Creating the textbox for the user to insert file location and type
        self.loc = StringVar()
        self.text_box = Entry(textvariable=self.loc, state=DISABLED)
        self.loc.set(EMPTY_STRING)

        # Creating a browse button
        self.browse_btn = Button(
            text=BROWSE_STRING,
            command=lambda: self._select_file(
                askopenfilenames(filetypes=FILE_TYPES)
            )
        )

        # Creating a button for user to submit the file to be converted to a PDF
        self.submit = Button(
            text=SUBMIT_STRING,
            command=lambda: self._convert_files()
        )

        # Oraganising the items in the Tk window
        self.label.grid(row=1, column=4, sticky='nsew', padx=10)
        self.status.grid(row=2, column=4, sticky='nsew', padx=10)
        self.text_box.grid(row=5, column=4, columnspan=8,
                           rowspan=2, sticky='nsew', padx=10)
        self.browse_btn.grid(row=8, column=4)
        self.submit.grid(row=9, column=4)
