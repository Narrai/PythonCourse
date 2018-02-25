from tkinter import *


class LabelDemo(Frame):

    def __init__(self):

        Frame.__init__(self)
        self.master.title("Label Demo")
        self.grid()
        self._label = Label(self, text='Hello World!')
        self._label.grid()


class ImageDemo(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.master.title("Image Demo")
        self.grid()
        self._image = PhotoImage(file="ball_100x100.png")
        print(self._image)
        self._imageLabel = Label(self, image=self._image)
        self._imageLabel.grid()
        self._textLabel = Label(self, text="Ball")
        self._textLabel.grid()


if __name__ == "__main__":
    # LabelDemo().mainloop()
    ImageDemo().mainloop()
