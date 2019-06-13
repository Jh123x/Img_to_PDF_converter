'''
PDF python toolkit to convert any type of image files into PDF format
Support for the following file types
    -JPG
    -PNG

Additional tools which are avaliable (Hopefully)
##TODO##
    -Reduce the size of the PDF File
    -Make PDF file clearer

Libraries used:
os for getting the locations for the files which are in question
tkinter for setting up the graphical user interface for the application
PILLOW for the management of the PDF and the other image files and applications in the app
'''


from PIL import Image,ImageDraw,ImageFilter
from tkinter import filedialog
import tkinter,os



#Classes
class window(tkinter.Frame):
    '''The main class for the tkinter window'''
    def __init__(self,master):
        self.master = master


def main():
    '''The main function for the PDF Toolkit in Python to run the GUI'''
    root = tkinter.Tk()
    gui = window(root)

    #Setting the size of the root window
    root.geometry("400x400")
    root.pack_propagate(0)
    root.resizable(0,0)

    #title of the window
    gui.master.title("PDF Toolkit")  

    #Creating the top Label for the GUI Window
    gui.label = tkinter.Label(text =  "PDF Toolkit")

    #Create a status bar to see the status
    gui.status_text = tkinter.StringVar()
    gui.status = tkinter.Label(textvariable = gui.status_text)
    gui.status_text.set("Locate the file by clicking the browse button and press submit")

    #Creating the textbox for the user to insert file location and type
    gui.loc = tkinter.StringVar()
    gui.text_box = tkinter.Entry(textvariable = gui.loc)
    gui.loc.set('')

    #Creating a browse button
    gui.browse_btn = tkinter.Button(text = "Browse", command = lambda: gui.loc.set(browse()))

    #Creating a button for user to submit the file to be converted to a PDF
    gui.submit = tkinter.Button(text = "Submit", command = lambda: gui.status_text.set(convert(gui.loc.get())))

    #Creating checkboxes for the GUI
    gui.checkbox = tkinter.Checkbutton()


    #Oraganising the items in the Tk window
    gui.label.grid(row = 1, column = 4)
    gui.status.grid(row = 2,column = 4)
    gui.browse_btn.grid(row = 6, column = 8)
    gui.text_box.grid(row = 5, column = 0,columnspan = 8, rowspan = 2)
    gui.submit.grid(row = 7, column = 8)

    root.mainloop()

def convert(file_loc):
    file_loc = eval(file_loc)
    try:
        image_o = Image.open(file_loc[0]).convert("RGB")
    except IOError as exp:
        return(exp,"\nThe file(s) is unable to be opened")
    except Exception as exp_obj:
        return("\n An Error has Occured: ",exp_obj)
    else:
        size = image_o.size
        output = Image.new('RGB',size,255)
        output.paste(image_o.copy())
        if len(file_loc) == 1:
            count = -1
            name = ''
            while file_loc[0][count] != '/':
                name = file_loc[0][count] + name
                count -= 1
            while '.' in name:
                name = name[:-1]
            output.save("Output/" + name + "_output.pdf","PDF",quality = 100,optimze = True)
            return "File converted successfully"
        else:
            imgs = [image_o]
            for i in file_loc:
                if file_loc.index(i) > 0:
                    count = -1
                    name = ''
                    while file_loc[0][count] != '/':
                        name = file_loc[0][count] + name
                        count -= 1
                    try:
                        imgs.append(Image.open(i).convert("RGB"))
                    except IOError as exp:
                        return (exp,"\nThe file is unable to be opened")
                    except Exception as exp:
                        return (exp,"\nAn Error has occured")
            output.save("Output/" + name + "and" +str(len(imgs)-1)+  "output.pdf","PDF",quality = 100, save_all = True, optimize = True, append_images = imgs[1:])
            return "Multiple files successfully converted"
        
        
        

def browse():
    '''Allows the user to input the file location by browsing through the folders'''
    loc =  filedialog.askopenfilenames()
    return loc


if __name__ == '__main__':
    main()
