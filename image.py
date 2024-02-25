from PIL import Image, ImageTk
from waifu2x_ncnn_py import Waifu2x

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
        self.new_image = self.img.copy()
        self.new_image.thumbnail((max,max))
        return ImageTk.PhotoImage(self.new_image)
    
    def save(self,path):
        """save image in folder with parameter name
        it's save with .png

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
    
    def scale_image(self, model, scale, noise):
        """scale image

        Args:
            model (string): type model {Anime, Photo}
            model (string): type {"x2","x4","x8"}
            noise (string): type {"Nothing", "Low","Medium","High", "Highest"}
        """

        model = "models-upconv_7_anime_style_art_rgb" if model == "Anime" else "models-upconv_7_photo"

        if scale == "x2":
            scale = 1
        elif scale == "x4":
            scale = 2
        elif scale == "x8":
            scale = 3

        if noise == "Nothing":
            noise = -1
        elif noise == "Low":
            noise = 0
        elif noise == "Medium":
            noise = 1
        elif noise == "High":
            noise = 2
        else:
            noise = 3

        #print(noise, size, model)
        waifu2x = Waifu2x(model=model, scale=2, noise=noise)
        for x in range(scale):
            self.img = waifu2x.process_pil(self.img)