import tkinter
import tkinter.filedialog as fd
import os



def get_folder_origem():
    root = tkinter.Tk()
    folder = fd.askdirectory(parent=root,initialdir="/",title='PLEASE SELECT THE SOURCE DIRECTORY OF THE IMAGES')
    if (os.path.isdir(folder)):
        return folder
    else:
        print("SOURCE DIRECTORY DOES NOT EXIST")




def get_folder_destination():
    root = tkinter.Tk()
    folder_des = fd.askdirectory(parent=root, initialdir="/", title='PLEASE SELECT THE DESTINATION DIRECTORY OF THE IMAGES')
    if (os.path.isdir(folder_des)):
        return folder_des
    else:
        print("SOURCE DIRECTORY DOES NOT EXIST")