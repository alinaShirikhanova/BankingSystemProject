from tkinter import *
import os
from PIL import Image, ImageTk


class LoginWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Sign Up')
        self.geometry('300x300-800+300')
        self.name = StringVar()
        self.login = StringVar()
        self.password = StringVar()
