from tkinter import BooleanVar, Frame, Label, Entry, Button, StringVar, Checkbutton, Tk
from tkinter.constants import DISABLED
from tkinter.filedialog import askopenfilenames

from Core import convert_files, combine_all_files
from Core.constants import NO_FILES_SELECTED
from GUI.constants import BROWSE_STRING, COMBINE_STRING, EMPTY_STRING, FILE_TYPES, LOADING_STRING, STICK_ALL, SUBMIT_STRING, DEFAULT_WINDOW_TITLE, INSTRUCTIONS


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

        # Default message to be shown when conerting
        self.status_text.set(LOADING_STRING)

        # If there are no files selected short circuit the function
        if self.selected_files is None or type(self.selected_files) is not tuple:
            self.status_text.set(NO_FILES_SELECTED)
            return

        # If the user wants to combine all the PDFs into one
        if self.is_combined.get():
            msg = combine_all_files(self.selected_files)
            self.status_text.set(msg)
            return

        # Default conversion of each file singly
        self.status_text.set(convert_files(self.selected_files))

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

        # Create a checkbox to see if the user wants to combine all the PDFs into one
        self.is_combined = BooleanVar(False)
        self.combine = Checkbutton(
            text=COMBINE_STRING, variable=self.is_combined)

        # Oraganising the items in the Tk window
        self.label.grid(row=1, column=4, sticky=STICK_ALL, padx=10)
        self.status.grid(row=2, column=4, sticky=STICK_ALL, padx=10)
        self.text_box.grid(row=5, column=4, columnspan=8,
                           rowspan=2, sticky=STICK_ALL, padx=10)
        self.combine.grid(row=7, column=4, sticky=STICK_ALL, padx=10)
        self.browse_btn.grid(row=8, column=4)
        self.submit.grid(row=9, column=4)
