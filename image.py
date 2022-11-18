from PIL import Image, ImageTk

class Img():
    def __init__(self, path) -> None:
        self.img = Image.open(path)

    def image_tkinter(self,max):
        self.new_image = self.img
        self.new_image.thumbnail((max,max))
        return ImageTk.PhotoImage(self.new_image)