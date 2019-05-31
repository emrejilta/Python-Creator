#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
import tkMessageBox
import os


class pyCreate(object):

    def __init__(self):
        try:
            self.fr = Frame()
            self.fr.pack(pady=5)

            self.e = Entry()
            self.e.pack()

            version = ["2.7", "3.6"]
            self.strn = StringVar()
            self.strn.set(version[0])
            self.om = OptionMenu(w, self.strn, *version)
            self.om.pack()

            self.bt = Button(text="Create", command=self.create)
            self.bt.pack()

        except IOError:
            self.lbl("Program doesn't work properly!")

    def lbl(self, msg):
        tkMessageBox.showinfo("Important", msg)

    def create(self):
        try:
            if not self.e.get():
                self.lbl("File name cannot be empty!")
            else:
                file = self.e.get() + ".py"
                vrs = self.strn.get()

            if "2.7" in vrs:
                header = "#!/usr/bin/env python\n"
            else:
                header = "#!/usr/bin/env python3\n"

            if not os.path.exists(file):
                f = open(file, "w")
                os.chmod(file, 0755)
                f.write(header)
                f.write("# -*- coding: utf-8 -*-\n")
                f.close()
            else:
                self.lbl(file + " exists!")
        except IOError:
            self.lbl("File cannot be created!")


if __name__ == '__main__':
    w = Tk()
    w.title("Python File Creator")
    w.geometry("220x120+500+200")
    w.resizable(width=FALSE, height=FALSE)
    py = pyCreate()

    mainloop()
