from PIL import Image, ImageTk

class Img():
    """manager the image
    """
    def __init__(self, path) -> None:
        self.img = Image.open(path)

    def image_tkinter(self,max)->ImageTk.PhotoImage:
        """tranform image for insert in tkinter

        Args:
            max (int):  width and height max the image for insert in tkinter

        Returns:
            ImageTk.PhotoImage: image for insert in tkinter
        """
        self.new_image = self.img
        self.new_image.thumbnail((max,max))
        return ImageTk.PhotoImage(self.new_image)
    
    def save(self,path):
        """save image in folder with parameter name
        it's save with .jpg

        Args:
            name (str, optional): name the image file. Defaults to "new".
        """
        self.img.save(path)
    
    def rotate(self, degrees):
        """rotate image and expand

        Args:
            degrees (int/float): degrees to rotate
        """
        self.img = self.img.rotate(degrees, expand=True)
    
    def black_white(self):
        """transfor color image in black and white
        """
        self.img = self.img.convert("L")